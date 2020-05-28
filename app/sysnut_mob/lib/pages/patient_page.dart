import 'package:flutter/material.dart';

class PatientPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text(
          "Pacientes",
          style: TextStyle(
            fontSize: 27,
            fontFamily: "Dancing Script",
          ),
        ),
      ),
      body: Container(
        child: ListView(
          children: <Widget>[
            Container(
              child: RaisedButton(
                color: Colors.green,
                child: Row(
                  children: <Widget>[
                    CircleAvatar(
                      radius: 30,
                      backgroundColor: Colors.transparent,
                      backgroundImage:
                          AssetImage("assets/images/nutricionist.png"),
                    ),
                    SizedBox(
                      width: 7,
                    ),
                    Text(
                      "Paula",
                      style: TextStyle(
                        fontSize: 13,
                        color: Colors.black54,
                      ),
                      textAlign: TextAlign.center,
                    ),
                    SizedBox(
                      width: 100,
                    ),
                    Container(
                      child: Column(
                        children: <Widget>[
                          Text(
                            "Próxima Consulta",
                            style: TextStyle(
                              fontSize: 13,
                              color: Colors.black54,
                            ),
                          ),
                          Text(
                            "11/06/2020",
                            style: TextStyle(
                              fontSize: 13,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
                onPressed: () {}, // Patient_Info
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(
          Icons.person_add,
        ),
        onPressed: () {},
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.endDocked,
    );
  }
}
