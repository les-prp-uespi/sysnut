import 'package:flutter/material.dart';

class MyButton extends StatelessWidget {
  final String name;
  final IconData myIcon;
  final Widget myPage;

  MyButton(this.name, this.myIcon, this.myPage);

  @override
  Widget build(BuildContext context) {
    return ButtonTheme(
      height: 145,
      minWidth: 150,
      child: RaisedButton(
        elevation: 10,
        child: Column(
          children: <Widget>[
            Icon(
              myIcon,
              size: 25,
              color: Colors.white,
            ),
            Text(
              name,
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
              builder: (context) => myPage,
            ),
          );
        },
      ),
    );
  }
}
