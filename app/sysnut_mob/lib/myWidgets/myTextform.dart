import 'package:flutter/material.dart';

class MyTextFormField extends StatelessWidget {

  final String myText;
  final TextInputType myInput;
  final bool myBool;

  MyTextFormField(this.myText,this.myInput,this.myBool);

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      keyboardType: myInput,
      obscureText: myBool,
      decoration: InputDecoration(
        labelText: myText,
        labelStyle: TextStyle(
          color: Colors.black38,
          fontWeight: FontWeight.w400,
          fontSize: 20,
        ),
      ),
      style: TextStyle(
        fontSize: 20,
      ),
    );
  }
}
