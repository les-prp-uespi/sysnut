# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import *
#DJANGO IMPORTS
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.core.urlresolvers import  reverse, reverse_lazy
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from django.db.models import Q
from dal import autocomplete
from sysnut.settings import LOGIN_URL
from os.path import join, dirname, abspath
import xlrd
import os
#from sysnut.nutritionist.views import is_nutritionist
import decimal
# Create your views here.

# class StaffRequiredMixin(object):
# 	#@method_decorator(login_required)
# 	def dispatch(self, request, *args, **kwargs):
# 		if not request.user.is_staff:
# 			messages.error(
# 				request,
# 				'Você não tem permissão para acessar esse link.')
# 			return redirect('core:index')
# 		return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)



class VitaminAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !

		qs = Vitamin.objects.all()

		# Pesquisa pela Descrição
		if self.q:
			qs = qs.filter(Q(description__icontains=self.q))

		return qs


#class SupplementAutocomplete(autocomplete.Select2QuerySetView):
#	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !

#		qs = Supplement.objects.all()

		# Pesquisa pela Descrição
#		if self.q:
#			qs = qs.filter(Q(description__icontains=self.q))

#		return qs

class PatologyAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !

		qs = Patology.objects.all()

		# Pesquisa pela Descrição
		if self.q:
			qs = qs.filter(Q(description__icontains=self.q))

		return qs

class GuidanceAuxAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !

		qs = GuidanceAux.objects.all()

		# Pesquisa pela Descrição
		if self.q:
			qs = qs.filter(Q(description__icontains=self.q))

		return qs

class GuidanceAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !

		qs = Guidance.objects.filter(nutritionist=self.request.user)

		# Pesquisa pela Descrição
		if self.q:
			qs = qs.filter(Q(description__icontains=self.q))

		return qs


class BiochemicalAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !

		qs = Biochemical.objects.all()

		# Pesquisa pela Descrição
		if self.q:
			qs = qs.filter(Q(description__icontains=self.q))

		return qs


# CRUD Patient
#@method_decorator(is_nutritionist, name='dispatch')
class PatientCreate(CreateView):

	model = Patient
	template_name = 'patient/new.html'
	form_class = PatientForm
	second_form_class = AddressForm

	def get(self, request, *args, **kwargs):
		self.object = None
		form = self.form_class
		address_form = self.second_form_class
		return self.render_to_response(
			self.get_context_data(
				form=form,
				address_form=address_form
			)
		)

	def post(self, request, *args, **kwargs):
		self.object = None
		address_form = self.second_form_class(self.request.POST)
		form = self.form_class(self.request.POST)

		if form.is_valid() and address_form.is_valid():
			messages.add_message(request, messages.SUCCESS, 'Paciente adicionado com sucesso!')
			return self.form_valid(form, address_form)
		else:
			return self.form_invalid(form, address_form)

	def form_valid(self, form, address_form):
		self.object = address_form.save()
		patient = form.save(commit=False)
		patient.address = self.object
		patient.user = self.request.user
		patient.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, address_form):
		return self.render_to_response(
			self.get_context_data(
					form=form,
                    address_form=address_form
			)
		)

	def get_success_url(self):
		return reverse('patient:list')

@method_decorator(login_required, name='dispatch')
class PatientUpdate(UpdateView):

	model = Patient
	template_name = 'patient/new.html'
	form_class = PatientForm
	second_form_class = AddressForm

	def get_context_data(self, **kwargs):
		self.object = self.get_object()
		context = super(PatientUpdate, self).get_context_data(**kwargs)
		if self.request.POST:
			context['address_form'] = self.second_form_class(self.request.POST, instance=self.object)
			context['form'] = self.form_class(self.request.POST, instance=self.object.address)
		else:
			context['address_form'] = self.second_form_class(instance=self.object.address)
			context['form'] = self.form_class(instance=self.object)

		return context

	def get(self, request, *args, **kwargs):
		super(PatientUpdate, self).get(request, *args, **kwargs)
		form = self.form_class
		address_form = self.second_form_class
		return self.render_to_response(
			self.get_context_data(
				object=self.object,
				form=form,
				address_form=address_form
			)
		)

	def post(self, request, *args, **kwargs):

		self.object = self.get_object()
		form = self.form_class(self.request.POST, instance=self.object)
		address_form = self.second_form_class(self.request.POST, instance=self.object.address)

		if form.is_valid() and address_form.is_valid():
			return self.form_valid(form, address_form)
		else:
			return self.form_invalid(form, address_form)

	def form_valid(self, form, address_form):
		self.object = address_form.save()
		patient = form.save(commit=False)
		patient.address = self.object
		patient.user = self.request.user
		patient.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, address_form):
		return self.render_to_response(
			self.get_context_data(
					form=form,
                    address_form=address_form
			)
		)

	def get_success_url(self):
		return reverse('patient:list')

@method_decorator(login_required, name='dispatch')
class PatientList(ListView):

	model = Patient
	http_method_names = ['get']
	template_name = 'patient/list.html'
	context_object_name = 'patient'
	paginate_by = 25

	def get_queryset(self):
		self.queryset = super(PatientList, self).get_queryset()
		if self.request.GET.get('search_box', False):
			if not self.request.user.is_superuser:
				self.queryset = self.queryset.filter(Q(user=self.request.user))
			self.queryset = self.queryset.filter(Q(first_name__icontains = self.request.GET['search_box']) | Q(last_name__icontains = self.request.GET['search_box']))
		else:
			if not self.request.user.is_superuser:
				self.queryset = self.queryset.filter(Q(user=self.request.user))
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(PatientList, self)
		context = _super.get_context_data(**kwargs)
		adjacent_pages = 3
		page_number = context['page_obj'].number
		num_pages = context['paginator'].num_pages
		startPage = max(page_number - adjacent_pages, 1)
		if startPage <= 5:
		    startPage = 1
		endPage = page_number + adjacent_pages + 1
		if endPage >= num_pages - 1:
		    endPage = num_pages + 1
		page_numbers = [n for n in range(startPage, endPage) \
				if n > 0 and n <= num_pages]
		context.update({
			'page_numbers': page_numbers,
			'show_first': 1 not in page_numbers,
			'show_last': num_pages not in page_numbers,
		    })
		return context

@method_decorator(login_required, name='dispatch')
class PatientDetail(DetailView):
	model = Patient
	template_name = 'patient/details.html'

	def get_context_data(self,**kwargs): 
		context = super(PatientDetail, self).get_context_data(**kwargs)
		if Consultation.objects.count() > 0:
			context = super(PatientDetail, self).get_context_data(**kwargs)
			context['consultation'] = []
			#Adiciona a consulta do paciente a uma lista
			for cons in self.object.patient_consultation.all():
				if(cons.patient.id == self.object.id):
					context['consultation'].append(cons)
		return context

@method_decorator(login_required, name='dispatch')
class PatientReport(DetailView):
	model = Patient
	template_name = 'patient/report.html'

	def get_context_data(self,**kwargs): 
		context = super(PatientReport, self).get_context_data(**kwargs)
		if Consultation.objects.count() > 0:
			context['consultation'] = []
			#Adiciona a consulta do paciente a uma lista
			for cons in self.object.patient_consultation.all():
				if(cons.patient.id == self.object.id):
					context['consultation'].append(cons)
		return context


@method_decorator(login_required, name='dispatch')
class PatientDelete(DeleteView):
	model = Patient
	success_url = reverse_lazy('patient:list')

#End CRUD Patient


# CRUD Consultation

@method_decorator(login_required, name='dispatch')
class ConsultationCreate(CreateView):
	model = Consultation
	template_name = 'consultation/new.html'
	form_class = ConsultationForm
	second_form_class = BodyCircunferenceForm
	third_form_class = EnergyCalcForm
	fourth_form_class = SkinFoldForm
	fifth_form_class = BioimpedanceForm
	sixth_form_class = BoneDiameterForm
	seventh_form_class = BiochemicalForm

	def get(self, request, *args, **kwargs):
		self.object = None
		self.exam_formset = ExamFormSet()
		form = self.form_class
		bodycirc_form = self.second_form_class
		energycalc_form = self.third_form_class
		skinfold_form = self.fourth_form_class
		bioimpedance_form = self.fifth_form_class
		bonediameter_form = self.sixth_form_class
		biochemical_form = self.seventh_form_class
		return self.render_to_response(
			self.get_context_data(
				form=form,
				bodycirc_form=bodycirc_form,
				energycalc_form=energycalc_form,
				skinfold_form=skinfold_form,
				bioimpedance_form=bioimpedance_form,
				bonediameter_form=bonediameter_form,
				biochemical_form=biochemical_form
			)
		)


	def post(self, request, *args, **kwargs):
		self.object = None
		bodycirc_form = self.second_form_class(self.request.POST)
		energycalc_form = self.third_form_class(self.request.POST)
		skinfold_form = self.fourth_form_class(self.request.POST)
		bioimpedance_form = self.fifth_form_class(self.request.POST)
		bonediameter_form = self.sixth_form_class(self.request.POST)
		biochemical_form = self.seventh_form_class(self.request.POST)
		form = self.get_form()
		self.exam_formset = ExamFormSet(self.request.POST, self.request.FILES)
		if form.is_valid() and bodycirc_form.is_valid() and energycalc_form.is_valid() and skinfold_form.is_valid() and bioimpedance_form.is_valid() and bonediameter_form.is_valid() and self.exam_formset.is_valid():
			return self.form_valid(form, bodycirc_form, energycalc_form, skinfold_form, bioimpedance_form, bonediameter_form, biochemical_form)
		else:
			return self.form_invalid(form, bodycirc_form, energycalc_form, skinfold_form, bioimpedance_form, bonediameter_form, biochemical_form)

	def form_valid(self, form, bodycirc_form, energycalc_form, skinfold_form, bioimpedance_form, bonediameter_form, biochemical_form):
		self.object = form.save(commit=False)
		self.object.patient = Patient.objects.get(id = self.kwargs['patient'])
		self.object.bodycirc = bodycirc_form.save()
		self.object.bioimpedance = bioimpedance_form.save()
		self.object.bonediameter = bonediameter_form.save()
		self.object.biochemical = biochemical_form.save(commit=False)
		self.object.energycalc = energycalc_form.save(commit=False)
		self.object.energycalc.mbr = decimal.Decimal(self.object.mbr())
		self.object.energycalc.tee = decimal.Decimal(self.object.tee())
		self.object.energycalc = energycalc_form.save()
		self.object.skinfold = skinfold_form.save()
		self.object.save()
		self.object.biochemical.consultation = self.object
		self.object.biochemical = biochemical_form.save(commit=False)
		#So deve criar o exame se a descricao for definida (não nulo)
		if (self.object.biochemical.exam is not None):
			self.object.biochemical.save()
		for item in form.cleaned_data['patology']:
			#print(item)
			self.object.patology.add(item)
		#for item in form.cleaned_data['supplement']:
		#	self.object.supplement.add(item)
		for item in form.cleaned_data['vitamin']:
			self.object.vitamin.add(item)
		self.exam_formset.instance = self.object
		self.exam_formset.save()
		messages.add_message(self.request, messages.SUCCESS, 'Consulta criada com sucesso!')
		return HttpResponseRedirect(reverse('patient:consultation_edit', kwargs={'pk':self.object.pk}))

	def form_invalid(self, form, bodycirc_form, energycalc_form, skinfold_form, bioimpedance_form, bonediameter_form, biochemical_form):
		return self.render_to_response(
			self.get_context_data(
					form=form,
                    bodycirc_form=bodycirc_form,
					energycalc_form=energycalc_form,
					skinfold_form=skinfold_form,
					bioimpedance_form=bioimpedance_form,
					bonediameter_form=bonediameter_form,
					biochemical_form=biochemical_form
			)
		)

	def get_context_data(self, **kwargs):
		context = super(ConsultationCreate,self).get_context_data(**kwargs)
		context['exam_formset'] = self.exam_formset
		context['patient_id'] = self.kwargs['patient']
		context['patient'] = Patient.objects.get(id = self.kwargs['patient'])
		return context


@method_decorator(login_required, name='dispatch')
class ConsultationList(ListView):

	model = Consultation
	http_method_names = ['get']
	template_name = 'consultation/list.html'
	context_object_name = 'consultation'
	paginate_by = 25

	def get_queryset(self):
		self.queryset = super(ConsultationList, self).get_queryset()
		self.queryset = self.queryset.filter(patient = self.kwargs['patient'])
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter(patient__name__icontains = self.request.GET['search_box'])
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(ConsultationList, self)
		context = _super.get_context_data(**kwargs)
		adjacent_pages = 3
		page_number = context['page_obj'].number
		num_pages = context['paginator'].num_pages
		startPage = max(page_number - adjacent_pages, 1)
		#Define o ID da consulta para o Template.
		context['patient_id'] = self.kwargs['patient']
		context['patient'] = Patient.objects.get(id=self.kwargs['patient'])
		if startPage <= 5:
		    startPage = 1
		endPage = page_number + adjacent_pages + 1
		if endPage >= num_pages - 1:
		    endPage = num_pages + 1
		page_numbers = [n for n in range(startPage, endPage) \
				if n > 0 and n <= num_pages]
		context.update({
			'page_numbers': page_numbers,
			'show_first': 1 not in page_numbers,
			'show_last': num_pages not in page_numbers,
		    })
		return context

@method_decorator(login_required, name='dispatch')
class ConsultationDetail(DetailView):
	model = Consultation
	template_name = 'consultation/details.html'

@method_decorator(login_required, name='dispatch')
class ConsultationUpdate(UpdateView):

	model = Consultation
	template_name = 'consultation/new.html'
	form_class = ConsultationForm
	second_form_class = BodyCircunferenceForm
	third_form_class = EnergyCalcForm
	fourth_form_class = SkinFoldForm
	fifth_form_class = BioimpedanceForm
	sixth_form_class = BoneDiameterForm
	seventh_form_class = BiochemicalForm


	def get_context_data(self, **kwargs):
		self.object = self.get_object()
		self.exam_formset = ExamFormSet(instance = self.object)
		context = super(ConsultationUpdate, self).get_context_data(**kwargs)
		context['exam_formset']=self.exam_formset
		context['patient_id'] = self.object.patient.id
		context['patient'] = Patient.objects.get(id = self.object.patient.id)
		if self.request.POST:
			context['bonediameter_form'] = self.sixth_form_class(self.request.POST, instance=self.object)
			context['bioimpedance_form'] = self.fifth_form_class(self.request.POST, instance=self.object)
			context['skinfold_form'] = self.fourth_form_class(self.request.POST, instance=self.object)
			context['energycalc_form'] = self.third_form_class(self.request.POST, instance=self.object)
			context['bodycirc_form'] = self.second_form_class(self.request.POST, instance=self.object)
			context['form'] = self.form_class(self.request.POST, instance=self.object.bodycirc)
		else:
			context['bonediameter_form'] = self.sixth_form_class(instance=self.object.bonediameter)
			context['bioimpedance_form'] = self.fifth_form_class(instance=self.object.bioimpedance)
			context['skinfold_form'] = self.fourth_form_class(instance=self.object.skinfold)
			context['energycalc_form'] = self.third_form_class(instance=self.object.energycalc)
			context['bodycirc_form'] = self.second_form_class(instance=self.object.bodycirc)
			context['form'] = self.form_class(instance=self.object)

		return context

	def get(self, request, *args, **kwargs):
		super(ConsultationUpdate, self).get(request, *args, **kwargs)
		form = self.form_class
		bodycirc_form = self.second_form_class
		energycalc_form = self.third_form_class
		skinfold_form = self.fourth_form_class
		bioimpedance_form = self.fifth_form_class
		bonediameter_form = self.sixth_form_class
		biochemical_form = self.seventh_form_class
		return self.render_to_response(
			self.get_context_data(
				object=self.object,
				form=form,
				bodycirc_form=bodycirc_form,
				energycalc_form=energycalc_form,
				skinfold_form=skinfold_form,
				bioimpedance_form=bioimpedance_form,
				bonediameter_form=bonediameter_form,
				biochemical_form=biochemical_form
			)
		)

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		self.exam_formset = ExamFormSet(self.request.POST, self.request.FILES, instance=self.object)
		bodycirc_form = self.second_form_class(self.request.POST)
		energycalc_form = self.third_form_class(self.request.POST)
		skinfold_form = self.fourth_form_class(self.request.POST)
		bioimpedance_form = self.fifth_form_class(self.request.POST)
		bonediameter_form = self.sixth_form_class(self.request.POST)
		biochemical_form = self.seventh_form_class(self.request.POST)
		form = self.get_form()
		if form.is_valid() and bodycirc_form.is_valid() and energycalc_form.is_valid() and skinfold_form.is_valid() and bioimpedance_form.is_valid() and bonediameter_form.is_valid() and biochemical_form.is_valid() and self.exam_formset.is_valid():
			return self.form_valid(form, bodycirc_form, energycalc_form, skinfold_form, bioimpedance_form, bonediameter_form, biochemical_form)
		else:
			return self.form_invalid(form, bodycirc_form, energycalc_form, skinfold_form, bioimpedance_form, bonediameter_form, biochemical_form)

	def form_valid(self, form, bodycirc_form, energycalc_form, skinfold_form, bioimpedance_form, bonediameter_form, biochemical_form):
		self.object = form.save(commit=False)
		self.object.bodycirc = bodycirc_form.save()
		self.object.bioimpedance = bioimpedance_form.save()
		self.object.bonediameter = bonediameter_form.save()
		self.object.biochemical = biochemical_form.save(commit=False)
		self.object.biochemical.consultation = self.object
		self.object.energycalc = energycalc_form.save(commit=False)
		self.object.energycalc.mbr = decimal.Decimal(self.object.mbr())
		self.object.energycalc.tee = self.object.tee()
		self.object.energycalc = energycalc_form.save()
		self.object.skinfold = skinfold_form.save()
		self.object.save()
		self.object.biochemical = biochemical_form.save(commit=False)
		#So deve criar o exame se a descricao for definida (não nulo)
		if (self.object.biochemical.exam is not None):
			self.object.biochemical.save()
		self.object.patology = {}
		#self.object.supplement = {}
		self.object.vitamin = {}
		for item in form.cleaned_data['patology']:
			self.object.patology.add(item)
		#for item in form.cleaned_data['supplement']:
		#	self.object.supplement.add(item)
		for item in form.cleaned_data['vitamin']:
			self.object.vitamin.add(item)
		self.exam_formset.instance = self.object
		self.exam_formset.save()
		
		return HttpResponseRedirect(reverse('patient:consultation_edit', kwargs={'pk':self.object.pk}))

	def form_invalid(self, form, bodycirc_form, energycalc_form, skinfold_form, bioimpedance_form, bonediameter_form):
		return self.render_to_response(
			self.get_context_data(
					form=form,
                    bodycirc_form=bodycirc_form,
                    energycalc_form=energycalc_form,
                    skinfold_form=skinfold_form,
                    bioimpedance_form=bioimpedance_form,
                    bonediameter_form=bonediameter_form,
                    biochemical_form=biochemical_form
			)
		)


@method_decorator(login_required, name='dispatch')
class ConsultationDelete(DeleteView):
	model = Consultation

	def delete(self, request, *args, **kwargs):
	    self.object = self.get_object()
	    id_return = self.object.patient.id
	    #print(">>>>>>>", id_return)
	    self.object.delete()
	    messages.add_message(self.request, messages.SUCCESS, 'Consulta removida com sucesso!')
	    return HttpResponseRedirect(reverse('patient:consultation_list', kwargs={'patient': id_return}))

def biochemical_delete(request, pk):
	biochemical = get_object_or_404(BiochemicalExam,id=pk)
	id_return = biochemical.consultation.id
	success_url = reverse('patient:consultation_edit', kwargs={'pk': id_return})

	if not request.user.is_superuser:
		messages.add_message(request, messages.INFO, 'Você precisa ser administrador para realizar esta ação.')
	else:
		biochemical.delete()
		messages.add_message(request, messages.SUCCESS, 'Exame removido com sucesso!')
	return HttpResponseRedirect(success_url)

class FoodAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !

		qs = Food.objects.all()

		# Pesquisa pela Descrição
		if self.q:
			qs = qs.filter(Q(description__icontains=self.q))
		#print(qs)
		return qs

@method_decorator(login_required, name='dispatch')
class UploadGuidance(CreateView):
    model = Guidance #Mudar de acordo com a tabela que receberá os dados da planilha
    template_name = 'analysis/upload_guidance.html'
    form_class = UploadGuidanceForm


    def form_valid(self, form):
        self.object = form.save(commit=False)
        #print(">>>>>> ", sheet.path)
        self.object.save()
        fname = join(dirname(abspath("media/" + str(self.object.path))),os.path.basename(str(self.object.path)))
        try:
            workbook = xlrd.open_workbook(fname)
        except:
            messages.add_message(self.request, messages.ERROR, 'Código 3! Formato de arquivo inválido!')
            return HttpResponseRedirect(reverse('patient:guidance_upload'))
        worksheet = workbook.sheet_by_name('Sheet1')
        worksheet = workbook.sheet_by_index(0)

        for row_num in range(worksheet.nrows):#le todas as linhas da planilha
        #for row_num in range(10):#le apenas as 10 primeiras linhas
    # cabeçalho
            if row_num == 0:
                continue
    		# Lê as linhas
            row = worksheet.row_values(row_num)
    		# Salva no banco
            if(GuidanceAux.objects.create(description=row[0],message=row[1],show=False)):
            	result = 1
            else:
                result = 0

        if(result == 1):
            messages.add_message(self.request, messages.SUCCESS, 'Orientações importadas com sucesso!')
        else:
            messages.add_message(self.request, messages.ERROR, 'Código 2! Algo de errado não está certo! Contate o administrador')
        return HttpResponseRedirect(reverse('core:index'))
            #return reverse('food:list')


# FoodAnalysis CRUD
@method_decorator(login_required, name='dispatch')
class FoodAnalysisList(ListView):

	model = FoodAnalysis
	http_method_names = ['get']
	template_name = 'analysis/list.html'
	context_object_name = 'analysis'
	paginate_by = 25

	def get_queryset(self):
		self.queryset = super(FoodAnalysisList, self).get_queryset()
		self.queryset = self.queryset.filter(consultation = self.kwargs['consultation'])
		if self.request.GET.get('search_box', False) :
			self.queryset=self.queryset.filter(title__icontains = self.request.GET['search_box'])
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(FoodAnalysisList, self)
		context = _super.get_context_data(**kwargs)
		adjacent_pages = 3
		page_number = context['page_obj'].number
		num_pages = context['paginator'].num_pages
		startPage = max(page_number - adjacent_pages, 1)
		#Define o ID da consulta para o Template.
		context['consultation_id'] = self.kwargs['consultation']
		context['consultation'] = Consultation.objects.get(id=context['consultation_id'])
		if startPage <= 5:
		    startPage = 1
		endPage = page_number + adjacent_pages + 1
		if endPage >= num_pages - 1:
		    endPage = num_pages + 1
		page_numbers = [n for n in range(startPage, endPage) \
				if n > 0 and n <= num_pages]
		context.update({
			'page_numbers': page_numbers,
			'show_first': 1 not in page_numbers,
			'show_last': num_pages not in page_numbers,
		    })
		return context

#@method_decorator(login_required, name='dispatch')
class FoodAnalysisDetail(DetailView):
	model = FoodAnalysis
	template_name = 'analysis/details.html'

class FoodAnalysisPrint(DetailView):
	model = FoodAnalysis
	template_name = 'analysis/print.html'

@method_decorator(login_required, name='dispatch')
class FoodAnalysisCreate(CreateView):
	model = FoodAnalysis
	template_name = 'analysis/new.html'
	form_class = FoodAnalysisForm
	second_form_class = MealForm
	third_form_class = SubstituteMealForm

	def get(self, request, *args, **kwargs):
		self.object = None
		self.consultation = Consultation.objects.get(id = self.kwargs['consultation'])
		form = self.form_class
		meal_form = self.second_form_class
		substitute_meal_form = self.third_form_class
		return self.render_to_response(
			self.get_context_data(
				form=form,
				meal_form=meal_form,
				substitute_meal_form=substitute_meal_form,
			)
		)

	def post(self, request, *args, **kwargs):
		self.object = None
		substitute_meal_form = self.third_form_class(self.request.POST)
		meal_form = self.second_form_class(self.request.POST)
		form = self.form_class(self.request.POST)
		if form.is_valid() and meal_form.is_valid():
			messages.add_message(request, messages.SUCCESS, 'Cardápio adicionado com sucesso!')
			return self.form_valid(form, meal_form, substitute_meal_form)
		else:
			return self.form_invalid(form, meal_form, substitute_meal_form)

	def form_valid(self, form, meal_form, substitute_meal_form):
		self.object = meal_form.save(commit=False)
		analysis = form.save(commit=False)
		analysis.consultation = Consultation.objects.get(id = self.kwargs['consultation'])
		analysis.save()
		substitute = substitute_meal_form.save(commit=False)
		substitute.food_analysis_substitute = analysis
		if substitute.food_substitute is not None:
			substitute.save()
		for item in form.cleaned_data['guidance']:
			analysis.guidance.add(item)
#		for item in form.cleaned_data['guidanceaux']:
#			analysis.guidanceaux.add(item)
		self.object.food_analysis = analysis
		#Verifica se existe alguma refeição cadastrada, se nao salva somente dados do cardapio
		if self.object.original_food is not None:
			self.object.save()
			return HttpResponseRedirect(reverse('patient:analysis_edit', kwargs={'pk':analysis.pk}))
		return HttpResponseRedirect(reverse('patient:analysis_list', kwargs={'consultation':analysis.consultation.id}))
		
	def form_invalid(self, form, meal_form, substitute_meal_form):
		return self.render_to_response(
			self.get_context_data(
					form=form,
                    meal_form=meal_form,
                    substitute_meal_form=substitute_meal_form,
			)
		)

	def get_context_data(self, **kwargs):
		context = super(FoodAnalysisCreate,self).get_context_data(**kwargs)
		context['consultation_id'] = self.kwargs['consultation']
		context['consultation'] = Consultation.objects.get(id = self.kwargs['consultation'])
		#context['guidanceaux_form'] = GuidanceAux.objects.all()
		return context

@method_decorator(login_required, name='dispatch')
class FoodAnalysisUpdate(UpdateView):
	model = FoodAnalysis
	template_name = 'analysis/new.html'
	form_class = FoodAnalysisForm
	second_form_class = MealForm
	third_form_class = SubstituteMealForm

	def get_context_data(self, **kwargs):
		self.object = self.get_object()
		context = super(FoodAnalysisUpdate, self).get_context_data(**kwargs)
		protein = self.object.protein()
		carb = self.object.carb()
		fat = self.object.total_fat()
		context['badge_protein'] = ""
		context['badge_carb'] = ""
		context['badge_fat'] = ""
		context['adequation_protein'] = (protein * 100 )/self.object.consultation.tee()
		context['adequation_carb'] = (carb * 100 )/self.object.consultation.tee()
		context['adequation_fat'] = (fat * 100 )/self.object.consultation.tee()
		if(self.object.consultation.nutrients == "OMS2008"):
			if context['adequation_fat'] < 10:
				context['badge_fat'] = "badge-warning"
			elif context['adequation_fat'] > 35:
				context['badge_fat'] = "badge-danger"
			else:
				context['badge_fat'] = "badge-success"

		else:
			if context['adequation_fat'] < 20:
				context['badge_fat'] = "badge-warning"
			elif context['adequation_fat'] > 35:
				context['badge_fat'] = "badge-danger"
			else:
				context['badge_fat'] = "badge-success"

			if context['adequation_carb'] > 65:
				context['badge_carb'] = "badge-danger"
			elif context['adequation_carb'] < 45:
				context['badge_carb'] = "badge-warning"
			else:
				context['badge_carb'] = "badge-success"

			if context['adequation_protein'] > 35:
				context['badge_protein'] = "badge-danger"
			elif context['adequation_protein'] < 10:
				context['badge_protein'] = "badge-warning"
			else:
				context['badge_protein'] = "badge-success"
				
		context['consultation_id'] = self.object.consultation.id
		context['consultation'] = Consultation.objects.get(id = self.object.consultation.id)
		if self.request.POST:
			#context['meal_form'] = self.second_form_class(self.request.POST, instance=self.object)
			context['form'] = self.form_class(self.request.POST, instance=self.object)

		else:
			#context['meal_form'] = self.second_form_class(instance=self.object)
			context['form'] = self.form_class(instance=self.object)

		return context

	def get(self, request, *args, **kwargs):
		super(FoodAnalysisUpdate, self).get(request, *args, **kwargs)
		form = self.form_class
		meal_form = self.second_form_class
		substitute_meal_form = self.third_form_class
		return self.render_to_response(
			self.get_context_data(
				object=self.object,
				form=form,
				meal_form=meal_form,
				substitute_meal_form=substitute_meal_form,
			)
		)

		return self.render_to_response(self.get_context_data())

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		meal_form = self.second_form_class(self.request.POST)
		substitute_meal_form = self.third_form_class(self.request.POST)
		form = self.form_class(self.request.POST, instance=self.object)

		if form.is_valid() and meal_form.is_valid() and substitute_meal_form.is_valid():
			return self.form_valid(form, meal_form, substitute_meal_form)
		else:
			return self.form_invalid(form, meal_form, substitute_meal_form)

	def form_valid(self, form, meal_form, substitute_meal_form):
		self.object = meal_form.save(commit=False)
		analysis = form.save(commit=False)
		analysis.guidance = {}
#		analysis.guidanceaux = {}
		for item in form.cleaned_data['guidance']:
			analysis.guidance.add(item)
#		for item in form.cleaned_data['guidanceaux']:
#			analysis.guidanceaux.add(item)
		analysis.save()
		self.object.food_analysis = analysis
		#Verifica se existe alguma refeição cadastrada, se nao salva somente dados do cardapio
		substitute = substitute_meal_form.save(commit=False)
		substitute.food_analysis_substitute = analysis
		save = 0
		if substitute.food_substitute is not None:
			substitute.save()
			save = 1
		if self.object.original_food is not None:
			self.object.save()
			save = 1
		if save == 1:
			messages.add_message(self.request, messages.SUCCESS, 'Refeição adicionada com sucesso!')
			return HttpResponseRedirect(reverse('patient:analysis_edit', kwargs={'pk':analysis.pk}))
		return HttpResponseRedirect(reverse('patient:analysis_list', kwargs={'consultation':analysis.consultation.id}))

	def form_invalid(self, form, meal_form):
		return self.render_to_response(
			self.get_context_data(
					form=form,
                    meal_form=meal_form,
			)
		)

	def get_success_url(self):
		return HttpResponseRedirect(reverse('patient:analysis_list', kwargs={'consultation': id_return}))

@method_decorator(login_required, name='dispatch')
class FoodAnalysisDelete(DeleteView):
	model = FoodAnalysis
	#success_url = reverse_lazy('patient:analysis_list')

	def delete(self, request, *args, **kwargs):
	    self.object = self.get_object()
	    id_return = self.object.consultation.id
	    #print(">>>>>>>", id_return)
	    self.object.delete()
	    messages.add_message(request, messages.SUCCESS, 'Cardápio removido com sucesso!')
	    return HttpResponseRedirect(reverse('patient:analysis_list', kwargs={'consultation': id_return}))

def publish_analysis(request, pk):
	analysis = get_object_or_404(FoodAnalysis,id=pk)
	id_return = analysis.consultation.id
	success_url = reverse('patient:analysis_list', kwargs={'consultation': id_return})
	val = ""

	if not request.user.is_authenticated:
		messages.add_message(request, messages.INFO, 'Você estar logado para realizar esta ação.')
	else:
		if(analysis.published == False):
			analysis.published = True
			val = "publicado"
		else:
			val = "despublicado"
			analysis.published = False
		analysis.save()
		messages.add_message(request, messages.SUCCESS, "Cardápio " + val + " com sucesso!")
	return HttpResponseRedirect(success_url)

def meal_delete(request, pk):
	meal = get_object_or_404(MealItem,id=pk)
	id_return = meal.food_analysis.id
	success_url = reverse('patient:analysis_edit', kwargs={'pk': id_return})

	if not request.user.is_authenticated:
		messages.add_message(request, messages.INFO, 'Você estar logado para realizar esta ação.')
	else:
		meal.delete()
		messages.add_message(request, messages.SUCCESS, 'Refeição removida com sucesso!')
	return HttpResponseRedirect(success_url)

# End FoodAnalysis CRUD

