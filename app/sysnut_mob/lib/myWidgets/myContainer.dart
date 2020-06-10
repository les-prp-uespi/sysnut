import 'package:flutter/material.dart';

class MyContainer extends StatelessWidget {
  final double myHeight;
  final double myWidth;
  final Alignment myAligment;
  final Alignment myBeginAligment;
  final Alignment myEndAligment;

  MyContainer(
    this.myHeight,
    this.myWidth,
    this.myAligment,
    this.myBeginAligment,
    this.myEndAligment,
  );

  @override
  Widget build(BuildContext context) {
    return Container(
      height: myHeight,
      width: myWidth,
      alignment: myAligment,
      decoration: BoxDecoration(
        gradient: LinearGradient(
          begin: myBeginAligment,
          end: myEndAligment,
          stops: [0.3, 0.7],
          colors: [
            Colors.deepPurple,
            Colors.purpleAccent,
          ],
        ),
        border: Border.all(
          width: 4.0,
          color: Colors.black38,
        ),
        borderRadius: BorderRadius.all(
          Radius.circular(56),
        ),
      ),
    );
  }
}
