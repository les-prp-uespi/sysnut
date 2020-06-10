import 'package:flutter/material.dart';
import 'package:sysnut_mob/myWidgets/myTextform.dart';
import './signup_page.dart';
import '../main.dart';

class LoginPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: EdgeInsets.only(top: 60, left: 40, right: 40),
        color: Colors.white,
        child: ListView(
          children: <Widget>[
            Column(
              children: <Widget>[
                SizedBox(
                  width: 128,
                  height: 128,
                  child: Image.asset("assets/images/iconnutri.png"),
                ),
                Text(
                  "SysNut",
                  style: TextStyle(
                    fontFamily: "Dancing Script",
                    fontSize: 35,
                  ),
                ),
              ],
            ),
            SizedBox(
              height: 25,
            ),
            MyTextFormField("email", TextInputType.emailAddress, false),
            SizedBox(
              height: 10,
            ),
            MyTextFormField("senha", TextInputType.text, true),
            Container(
              height: 40,
              alignment: Alignment.centerRight,
              child: FlatButton(
                child: Text(
                  "Recuperar Senha",
                  textAlign: TextAlign.right,
                ),
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => LoginPage(), // ResetPasswordPage()
                    ),
                  );
                },
              ),
            ),
            SizedBox(
              height: 60,
            ),
            Container(
              height: 60,
              alignment: Alignment.centerLeft,
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                  stops: [0.3, 1],
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
                    "Login",
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                      fontSize: 20,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => MyHomePage(),
                      ),
                    );
                  },
                ),
              ),
            ),
            SizedBox(
              height: 20,
            ),
            Container(
              height: 40,
              child: FlatButton(
                child: Text(
                  "Cadastrar-se",
                  textAlign: TextAlign.center,
                ),
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => SignupPage(), // SignupPage
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
