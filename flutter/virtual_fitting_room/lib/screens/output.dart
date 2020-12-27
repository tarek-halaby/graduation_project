import 'dart:async';
import 'dart:io';
import 'dart:typed_data';
//import 'package:image/image.dart' as I; //So that this does not conflict with the Image widget

import 'package:flutter/material.dart';
class output extends StatelessWidget {
  Uint8List imag;
  Image outputImage;
//  I.Image _img;
  output(Uint8List image)
  {
    imag=image;
    outputImage =new Image.memory(imag) ;
//      outputImage= MemoryImage(imag);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: true,
        backgroundColor: Colors.black,
        title: Text(
          "Virtual Fitting Room",
          style: TextStyle(color: Colors.white),),
      ),
      body: Center(
        child:Container(
            child: outputImage
        ) ,
      ));
  }
}