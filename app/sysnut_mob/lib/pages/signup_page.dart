import 'package:flutter/material.dart';
import 'package:sysnut_mob/myWidgets/myTextform.dart';
import '../main.dart';

class SignupPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: EdgeInsets.only(
          top: 10,
          left: 40,
          right: 40,
        ),
        color: Colors.white,
        child: ListView(
          children: <Widget>[
            Container(
              width: 160,
              height: 160,
              alignment: Alignment(0.0, 1.15),
              decoration: new BoxDecoration(
                image: new DecorationImage(
                  image: AssetImage("assets/images/image_icon.png"),
                  fit: BoxFit.fitHeight,
                ),
              ),
              child: Container(
                height: 56,
                width: 56,
                alignment: Alignment.center,
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                    stops: [0.3, 0.7],
                    colors: [
                      Colors.deepPurple,
                      Colors.purpleAccent,
                    ],
                  ),
                  border: Border.all(
                    width: 4.0,
                    color: Colors.black38,
                  ),
                  borderRadius: BorderRadius.all(
                    Radius.circular(56),
                  ),
                ),
                child: SizedBox.expand(
                  child: Padding(
                    padding: const EdgeInsets.all(0),
                    child: FlatButton(
                      child: Icon(
                        Icons.photo_camera,
                        color: Colors.white,
                      ),
                      onPressed: () {},
                    ),
                  ),
                ),
              ),
            ),
            SizedBox(
              height: 20,
            ),
            MyTextFormField("Usuário", TextInputType.text,false),
            SizedBox(
              height: 10,
            ),
            MyTextFormField("Nome Completo", TextInputType.text,false),
            SizedBox(
              height: 10,
            ),
            MyTextFormField("email", TextInputType.emailAddress,false),
            SizedBox(
              height: 10,
            ),
            MyTextFormField("CRN", TextInputType.number,false),
            SizedBox(
              height: 10,
            ),
            MyTextFormField("Data de Nascimento", TextInputType.datetime,false),
            SizedBox(
              height: 10,
            ),
            MyTextFormField("telefone", TextInputType.number,false),
            SizedBox(
              height: 10,
            ),
            MyTextFormField("Senha",TextInputType.text,false),
            SizedBox(
              height: 10,
            ),
             MyTextFormField("Confirmar Senha",TextInputType.text,false),
            SizedBox(
              height: 10,
            ),
            Container(
              height: 60,
              alignment: Alignment.centerLeft,
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                  stops: [0.3, 1.0],
                  colors: [
                    Colors.deepPurple,
                    Colors.purpleAccent,
                  ],
                ),
                borderRadius: BorderRadius.all(
                  Radius.circular(5),
                ),
              ),
              child: SizedBox.expand(
                child: FlatButton(
                  child: Text(
                    "Cadastrar-se",
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                      fontSize: 20,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  onPressed: () => Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => MyHomePage(),
                    ),
                  ),
                ),
              ),
            ),
            SizedBox(
              height: 10,
            ),
            Container(
              height: 40,
              alignment: Alignment.center,
              child: FlatButton(
                child: Text(
                  "Cancelar",
                  textAlign: TextAlign.center,
                ),
                onPressed: () => Navigator.pop(context, false),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
