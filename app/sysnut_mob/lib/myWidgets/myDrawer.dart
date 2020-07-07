import 'package:flutter/material.dart';
import 'package:sysnut_mob/pages/login_page.dart';
import 'myListTile.dart';

class MyDrawer extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: Container(
        color: Colors.deepPurple,
        child: ListView(
          children: <Widget>[
            MyListTile(
              MyCircleAvatar(),
              MyText("Olá Dr. Ana", 20),
              MyIconButton(Icons.close),
            ),
            SizedBox(
              height: 25,
            ),
            MyListTile(
              MyIconButton(Icons.settings),
              MyText("Configurações", 17),
            ),
            MyListTile(
              MyIconButton(Icons.help),
              MyText("Instruções de Uso", 17),
            ),
            MyListTile(
              MyIconButton(Icons.content_paste),
              MyText("Avalie-nos", 17),
            ),
            MyListTile(
              FlatButton(
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
                    MaterialPageRoute(builder: (context) => LoginPage()),
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
