import 'package:flutter/material.dart';
import 'pages/login_page.dart';
import 'pages/patient_page.dart';

main() => runApp(SysnutApp());

class SysnutApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Sysnut',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
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
        title: Text(
          "SysNut",
          style: TextStyle(
            fontFamily: "Dancing Script",
            fontSize: 27,
          ),
          textAlign: TextAlign.center,
        ),
        actions: <Widget>[
          IconButton(
            icon: Icon(Icons.list),
            onPressed: () {},
            alignment: Alignment.center,
          ),
        ],
      ),
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
                        RaisedButton(
                          elevation: 10,
                          child: Column(
                            children: <Widget>[
                              Icon(
                                Icons.person,
                                size: 25,
                                color: Colors.white,
                              ),
                              Text(
                                "Pacientes",
                                style: TextStyle(
                                  fontSize: 25,
                                  fontFamily: "Dancing Script",
                                  color: Colors.white,
                                ),
                              ),
                            ],
                          ),
                          onPressed: () {
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) => PatientPage(),
                              ),
                            );
                          },
                        ),
                        SizedBox(
                          width: 10,
                        ),
                        RaisedButton(
                          elevation: 10,
                          child: Column(
                            children: <Widget>[
                              Icon(
                                Icons.fastfood,
                                size: 25,
                                color: Colors.white,
                              ),
                              Text(
                                "Alimentos",
                                style: TextStyle(
                                  fontSize: 25,
                                  fontFamily: "Dancing Script",
                                  color: Colors.white,
                                ),
                              ),
                            ],
                          ),
                          onPressed: () {
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) =>
                                    LoginPage(), // AlimentPage
                              ),
                            );
                          },
                        ),
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
                        RaisedButton(
                          elevation: 10,
                          child: Column(
                            children: <Widget>[
                               Icon(
                                Icons.insert_drive_file,
                                size: 25,
                                color: Colors.white,
                              ),
                              Text(
                                "Orientações",
                                style: TextStyle(
                                  fontSize: 25,
                                  fontFamily: "Dancing Script",
                                  color: Colors.white,
                                ),
                              ),
                            ],
                          ),
                          onPressed: () {
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) =>
                                    LoginPage(), //OrientationPage
                              ),
                            );
                          },
                        ),
                        SizedBox(
                          width: 10,
                        ),
                        RaisedButton(
                          elevation: 10,
                          child: Column(
                            children: <Widget>[
                               Icon(
                                Icons.phone_android,
                                size: 25,
                                color: Colors.white,
                              ),
                              Text(
                                "Calculadora",
                                style: TextStyle(
                                  fontSize: 25,
                                  fontFamily: "Dancing Script",
                                  color: Colors.white,
                                ),
                              ),
                            ],
                          ),
                          onPressed: () {
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) => LoginPage(), //CalcPage
                              ),
                            );
                          },
                        ),
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
