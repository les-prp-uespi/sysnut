import 'package:flutter/material.dart';

class MyContainer extends StatelessWidget {
  final double MyHeight;
  final double MyWidth;
  final Alignment MyAligment;
  final Alignment MyBeginAligment;
  final Alignment MyEndAligment;

  MyContainer(
    this.MyHeight,
    this.MyWidth,
    this.MyAligment,
    this.MyBeginAligment,
    this.MyEndAligment,
  );

  @override
  Widget build(BuildContext context) {
    return Container(
      height: MyHeight,
      width: MyWidth,
      alignment: MyAligment,
      decoration: BoxDecoration(
        gradient: LinearGradient(
          begin: MyBeginAligment,
          end: MyEndAligment,
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
