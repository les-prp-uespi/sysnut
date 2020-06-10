import 'package:flutter/material.dart';

class MyListTile extends StatelessWidget {
  final Widget myWidget;
  final String myText;
  final IconData myIcon;
  final double mySize;

  MyListTile(
    this.myText,
    this.myIcon,
    this.mySize,
    [this.myWidget]
  );

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: myWidget,
      title: Text(
        myText,
        style: TextStyle(
          color: Colors.white,
          fontSize: mySize,
        ),
      ),
      trailing: IconButton(
        icon: Icon(
          myIcon,
          color: Colors.white,
        ),
        onPressed: () => Navigator.pop(context, false),
      ),
    );
  }
}

class MyCircleAvatar extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return CircleAvatar(
      radius: 30,
      backgroundColor: Colors.transparent,
      backgroundImage: AssetImage("assets/images/nutricionist.png"),
    );
  }
}

class MyIcon extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      
    );
  }
}


