import 'package:flutter/material.dart';
import 'package:sysnut_mob/pages/login_page.dart';
import 'myLIstTile.dart';

class MyDrawer extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Drawer(
        child: Container(
          color: Colors.deepPurple,
          child: ListView(
            children: <Widget>[
              MyListTile(
                "Olá Dr Ana",
                Icons.close,
                20,
                MyCircleAvatar(),
              ),
              SizedBox(
                height: 25,
              ),
              MyListTile(
                "Configurações",
                Icons.settings,
                17,
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
                        builder: (context) => LoginPage()
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