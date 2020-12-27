import 'dart:convert';
import 'dart:typed_data';
import 'package:http/http.dart' as http;
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:virtual_fitting_room/widgets/body_measurements_background.dart';
import 'dart:io' as Io;
import 'package:image_picker/image_picker.dart';
class bodyMeasurements extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return bodyMeasurementsStatefulWidget();
  }
}

class bodyMeasurementsStatefulWidget extends StatefulWidget {
  bodyMeasurementsStatefulWidget({Key key}) : super(key: key);

  @override
  bodyMeasurementsStatefulWidgetState createState() => bodyMeasurementsStatefulWidgetState();
}
class bodyMeasurementsStatefulWidgetState extends State<bodyMeasurementsStatefulWidget> {

  final List<String> images=['weight.jpg','height.jpg'];
  final List<String> items=['Weight','Height'];
  @override
  Widget build(BuildContext context) {
    double _height = MediaQuery
        .of(context)
        .size
        .height;
    double _width = MediaQuery
        .of(context)
        .size
        .width;
    return Scaffold(
        backgroundColor: Colors.white,

        appBar: AppBar(
        title: Text("Virtual Fitting Room"),
        backgroundColor: Color(0xFF9F140B),
        centerTitle: true,

      ),
        bottomNavigationBar: Container(
            height:_height*0.07,
            child: RaisedButton(
                onPressed: () {
//                  _imgFromGallery(context);
                },
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius
                      .circular(5.0),
                  side:
                  BorderSide(color: Color(
                      0xFF9F140B))),
              color: Color(0xFF9F140B),
              child: Text(
                "Submit",
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 25,
                ),
              ),
            )),
      body: Container(
        height: _height-AppBar().preferredSize.height,
    width: _width,
    child:CustomPaint(
        size: Size(_width, _height-AppBar().preferredSize.height),
        painter: CurvePainter(),

      child:Container(
      margin: EdgeInsets.only(top: _height*0.02),
      child:ListView.builder(

    itemCount: items.length,
    itemBuilder: (context, index) {
      return Column(children: [

            Container(
                    width: _width*0.85,
                    height: _height*0.15,
                      child:Row(
            children: [

              Expanded(
                      flex: 7,
                      child:Column(
                  children:[
                    Expanded(
                flex: 2,
                child: Container(alignment:Alignment.centerLeft,child:Text(items[index]+" : ",
                style: TextStyle(fontSize: 17,fontWeight: FontWeight.bold),),)
              ),
              Expanded(
                flex: 1,
                child: Container(),
              ),
              Expanded(
                flex: 2,
                child: Row(children: [
                  Container(
                  height: _height*0.15,
                  width: _width*0.2,
                  alignment: Alignment.centerLeft,
                  child: TextField(

                    style: TextStyle(fontSize: 20,fontWeight: FontWeight.bold,),
                    textAlign: TextAlign.center,
                    decoration: new InputDecoration(
                      errorBorder: OutlineInputBorder(
                        borderSide: BorderSide(width: 0.2),
                      ),
                      focusedErrorBorder: OutlineInputBorder(
                        borderSide: BorderSide(width: 0.2),
                      ),
                      focusedBorder: OutlineInputBorder(
                        borderSide: BorderSide(width: 0.2),
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderSide: BorderSide( width: 0.2),
                      ),),

                  ),
                ),
                Expanded(
                    flex: 3,
                    child:Container(
                    alignment: Alignment.centerLeft,
                    child:Center(child: Text(" cm"),),
                  )),
                  Expanded(
                    flex: 3,
                    child: Container(),
                  )
              ]),
              ),
                    Expanded(
                      flex: 1,
                      child: Container(),
                    ),
                  ])),
              Expanded(
                flex: 4,
                child: ClipOval(
                  child:Material(
                      child: SizedBox(width: _height*0.13, height: _height*0.13, child: Image.asset('assets/'+images[index],fit: BoxFit.fill,)),
                    ),
                ),
              ),
              Expanded(
                flex: 1,
                child: Container(),
              ),
            ],
          )
        ),

        new Divider(
          thickness: 2,
        )
      ]);
    })
    ))));
  }
  Io.File image;
  ImagePicker imagePicker = ImagePicker();

  _imgFromGallery(BuildContext context) async {
    PickedFile pickedFile =
    await imagePicker.getImage(source: ImageSource.gallery);
    if (pickedFile != null) {
      image = Io.File(pickedFile.path);
      Uint8List res = await upload_image(image);
//      Navigator.push(
//        context,
//        MaterialPageRoute(builder: (context) => output(res)),
//      );
    }
  }

  upload_image(Io.File imageFile) async {
    List<int> imageBytes = await Io.File(imageFile.path).readAsBytes();
    String base64Encode = base64.encode(imageBytes);
    var image = {"image": "${base64Encode}"};
    var body = image;
    var response = await http.post(
        Uri.parse("https://virtual--fitting--room.herokuapp.com/upload-image"),
        body: jsonEncode(body),
        headers: {"content-type": "application/json"});
    var jsonResponse = jsonDecode(response.body);
    var processing = jsonResponse["processing"];
    print (processing);
    var wait = {"wait": "1"};
    await sleep1();
    var response2 = await http.post(
        Uri.parse("https://virtual--fitting--room.herokuapp.com/upload-image"),
        body: jsonEncode(wait),
        headers: {"content-type": "application/json"});
    var jsonResponse2 = jsonDecode(response2.body);
    var image64 = jsonResponse2["image"];
    Uint8List bytes = base64.decode(image64);
    return bytes;
  }
  Future sleep1() {
    return new Future.delayed(const Duration(seconds: 60));
  }
}
