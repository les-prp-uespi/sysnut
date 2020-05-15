import 'package:flutter/material.dart';
import 'pages/login_page.dart';

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
        backgroundColor: Colors.purple,
        title: Padding(
          padding: const EdgeInsets.all(70),
          child: Text(
            "SysNut",
            style: TextStyle(
              fontFamily: "Dancing Script",
              fontSize: 27,
              color: Colors.black,
            ),
            textAlign: TextAlign.center,
          ),
        ),
        actions: <Widget>[
          IconButton(
            icon: Icon(Icons.home),
            onPressed: () {},
            alignment: Alignment.center,
          ),
        ],
      ),
      body: Container(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.start,
          children: <Widget>[
            Column(
              mainAxisAlignment: MainAxisAlignment.end,
              children: <Widget>[
                SizedBox(
                  height: 450,
                ),
                RaisedButton(
                  color: Colors.purpleAccent,
                  elevation: 5,
                  child: Text(
                    "Pacientes",
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.w400,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  onPressed: () {},
                ),
                RaisedButton(
                  color: Colors.purpleAccent,
                  elevation: 5,
                  child: Text(
                    "Orientações",
                    style: TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.w400,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  onPressed: () {},
                ),
              ],
            ),
            Column(
              mainAxisAlignment: MainAxisAlignment.end,
              children: <Widget>[
                SizedBox(
                  height: 450,
                ),
                RaisedButton(
                  color: Colors.purpleAccent,
                  elevation: 5,
                  child: Text(
                    "Alimentos",
                    style: TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.w400,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  onPressed: () {},
                ),
                RaisedButton(
                  color: Colors.purpleAccent,
                  elevation: 5,
                  child: Text(
                    "Calculadora",
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.w400,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  onPressed: () {},
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
