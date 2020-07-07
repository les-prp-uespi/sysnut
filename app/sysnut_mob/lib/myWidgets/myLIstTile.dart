import 'package:flutter/material.dart';

class MyListTile extends StatelessWidget {
  final Widget myLeading;
  final Widget mytitle;
  final Widget myTrailing;

  MyListTile([this.myLeading, this.mytitle, this.myTrailing]);

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: myLeading,
      title: mytitle,
      trailing: myTrailing,
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

class MyIconButton extends StatelessWidget {
  final IconData myIcon;
  MyIconButton(this.myIcon);

  @override
  Widget build(BuildContext context) {
    return IconButton(
      icon: Icon(
        myIcon,
        color: Colors.white,
      ),
      onPressed: () => Navigator.pop(context, false),
    );
  }
}

class MyText extends StatelessWidget {
  final String myText;
  final double mySize;
  MyText(this.myText, this.mySize);

  @override
  Widget build(BuildContext context) {
    return Text(
      myText,
      style: TextStyle(
        color: Colors.white,
        fontSize: mySize,
      ),
    );
  }
}
