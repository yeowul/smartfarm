import 'package:flutter/material.dart';

import 'main.dart';

void main() => runApp(MaterialApp(
      title: "App",
      home: CalendarRoute(),
    ));

class CalendarRoute extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text('calendar Route'),
      ),
      body: Center(
        child: OutlinedButton(
          child: Text('Move Main route'),
          onPressed: () {
            Navigator.push(
                context, MaterialPageRoute(builder: (context) => MainRoute()));
          },
        ),
      ),
    );
  }
}
