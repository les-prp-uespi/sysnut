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
        primarySwatch: Colors.blue,
      ),
      home: LoginPage(),
    );
  }
}