import 'package:flutter/material.dart';
import 'myWidgets/myDrawer.dart';
import 'pages/login_page.dart';
import 'pages/patient_page.dart';
import './myWidgets/myButton.dart';

main() => runApp(SysnutApp());

class SysnutApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Sysnut',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
        accentIconTheme: IconThemeData(
          color: Colors.white,
          size: 25,
        ),
      ),
      home: LoginPage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        leading: new IconButton(
          icon: new Icon(Icons.list),
          onPressed: () => Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => MyDrawer(),
            ),
          ),
          alignment: Alignment.center,
        ),
        title: Text(
          "SysNut",
          style: TextStyle(
            fontFamily: "Dancing Script",
            fontSize: 27,
          ),
          textAlign: TextAlign.center,
        ),
      ),
      drawer: MyDrawer(),
      //
      //
      //
      body: Container(
        child: Column(
          children: <Widget>[
            Container(
              alignment: Alignment.topCenter,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: <Widget>[
                  CircleAvatar(
                    radius: 60,
                    backgroundColor: Colors.transparent,
                    backgroundImage:
                        AssetImage("assets/images/nutricionist.png"),
                  ),
                  Text(
                    "Bem Vindo de Volta",
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.w400,
                    ),
                  ),
                  Text(
                    "Dr. Ana",
                    style: TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.w400,
                    ),
                  ),
                  SizedBox(
                    height: 10,
                  ),
                  Text(
                    "O que Faremos Hoje ?",
                    style: TextStyle(
                      fontSize: 17,
                      fontWeight: FontWeight.bold,
                    ),
                    textAlign: TextAlign.center,
                  ),
                ],
              ),
            ),
            SizedBox(
              height: 30,
            ),
            Container(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  ButtonTheme(
                    height: 145,
                    minWidth: 150,
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        MyButton("Pacientes", Icons.person, PatientPage()),
                        SizedBox(
                          width: 10,
                        ),
                        MyButton("Alimentos", Icons.fastfood, LoginPage()),
                      ],
                    ),
                  ),
                  SizedBox(
                    height: 15,
                  ),
                  ButtonTheme(
                    height: 145,
                    minWidth: 150,
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        MyButton("Orientações", Icons.insert_drive_file,
                            LoginPage()),
                        SizedBox(
                          width: 10,
                        ),
                        MyButton(
                            "Calculadora", Icons.phone_android, LoginPage()),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
