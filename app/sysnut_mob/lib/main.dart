import 'package:flutter/material.dart';
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
    Widget sideBar() {
      return Drawer(
        child: Container(
          color: Colors.deepPurple,
          child: ListView(
            children: <Widget>[
              new ListTile(
                leading: CircleAvatar(
                  radius: 30,
                  backgroundColor: Colors.transparent,
                  backgroundImage: AssetImage("assets/images/nutricionist.png"),
                ),
                title: Text(
                  "Olá Dr Ana",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 20,
                  ),
                ),
                trailing: IconButton(
                  icon: Icon(
                    Icons.close,
                    color: Colors.white,
                  ),
                  onPressed: () => Navigator.pop(context, false),
                ),
              ),
              SizedBox(
                height: 25,
              ),
              new ListTile(
                leading: Icon(
                  Icons.settings,
                  color: Colors.white,
                ),
                title: Text(
                  "Configurações",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 17,
                  ),
                ),
              ),
              new ListTile(
                leading: Icon(
                  Icons.help,
                  color: Colors.white,
                ),
                title: Text(
                  "Instruções de Uso",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 17,
                  ),
                ),
              ),
              new ListTile(
                leading: Icon(
                  Icons.content_paste,
                  color: Colors.white,
                ),
                title: Text(
                  "Avalie-nos",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 17,
                  ),
                ),
              ),
              new ListTile(
                leading: FlatButton(
                  child: Text(
                    "Sair",
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 17,
                    ),
                  ),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => LoginPage(),
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

    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        leading: new IconButton(
          icon: new Icon(Icons.list),
          onPressed: () => Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => sideBar(),
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
      drawer: sideBar(),
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
                        MyButton("Pacientes",Icons.person,PatientPage),
                        SizedBox(
                          width: 10,
                        ),
                        MyButton("Alimentos",Icons.fastfood, LoginPage),
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
                        MyButton("Orientações",Icons.insert_drive_file,LoginPage),
                        SizedBox(
                          width: 10,
                        ),
                        MyButton("Calculadora",Icons.phone_android,LoginPage),
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
