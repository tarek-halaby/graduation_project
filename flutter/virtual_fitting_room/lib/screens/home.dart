import 'package:flutter/material.dart';
import 'package:virtual_fitting_room/screens/body_measurements.dart';
import 'package:virtual_fitting_room/screens/login.dart';

class home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,

        appBar: AppBar(
        leading: IconButton(
          icon: Icon(Icons.logout),
          onPressed: () {
            Navigator.pop(context);
            Navigator.push(
                context,
                MaterialPageRoute(
                    builder: (context)
                    =>
                        login()
                ));
          },
        ),
        centerTitle: true,
        title: Text("Virtual Fitting Room"),
        backgroundColor: Color(0xFF9F140B),
      ),
      body: Builder(
        builder: (BuildContext context) {
          double _height = MediaQuery
              .of(context)
              .size
              .height;
          double _width = MediaQuery
              .of(context)
              .size
              .width;
          return ListView(children: <Widget>[
            SizedBox(height: _height * 0.025),
            Container(
              child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: <Widget>[

                    SizedBox(height: _height * 0.15,),


                    Container(
                        child: Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            crossAxisAlignment: CrossAxisAlignment.center,
                            children: <Widget>[
                              Container(
                                  child: Column(
                                      mainAxisAlignment: MainAxisAlignment
                                          .center,
                                      crossAxisAlignment: CrossAxisAlignment
                                          .center,
                                      children: <Widget>[
                                        Container(
                                            child: Text("Front View")
                                        ),
                                        Container(
                                            child: Image.asset(
                                              'assets/frontView.png',
                                              height: _height * 0.2,)
                                        ),
                                        new Container(
                                            height: _height * 0.05,
                                            child: RaisedButton(

                                              onPressed: () async {},
                                              shape: RoundedRectangleBorder(
                                                  borderRadius: BorderRadius
                                                      .circular(5.0),
                                                  side:
                                                  BorderSide(color: Color(
                                                      0xFF9F140B))),
                                              color: Color(0xFF9F140B),
                                              child: Text(
                                                "Upload front",
                                                style: TextStyle(
                                                  color: Colors.white,
                                                  fontSize: 20,
                                                ),
                                              ),
                                            )),
                                      ])
                              ),
                              SizedBox(width: _width * 0.15,),
                              Container(
                                  child: Column(
                                      mainAxisAlignment: MainAxisAlignment
                                          .center,
                                      crossAxisAlignment: CrossAxisAlignment
                                          .center,
                                      children: <Widget>[
                                        Container(
                                            child: Text("Side View")
                                        ),
                                        Container(
                                            child: Image.asset(
                                              'assets/sideView.png',
                                              height: _height * 0.2,)
                                        ),
                                        new Container(
                                            height: _height * 0.05,
                                            child: RaisedButton(

                                              onPressed: () async {},
                                              shape: RoundedRectangleBorder(
                                                  borderRadius: BorderRadius
                                                      .circular(5.0),
                                                  side:
                                                  BorderSide(color: Color(
                                                      0xFF9F140B))),
                                              color: Color(0xFF9F140B),
                                              child: Text(
                                                "Upload side",
                                                style: TextStyle(
                                                  color: Colors.white,
                                                  fontSize: 20,
                                                ),
                                              ),
                                            )),
                                      ])
                              ),
                            ])
                    ),
                      SizedBox(height: _height*0.15,),
                    new Container(
                        height: _height * 0.05,
                        child: RaisedButton(

                          onPressed: ()  {
                            Navigator.push(
                                context,
                                MaterialPageRoute(
                                    builder: (context)
                                    =>
                                        bodyMeasurements()
                                ));
                          },
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius
                                  .circular(5.0),
                              side:
                              BorderSide(color: Color(
                                  0xFF9F140B))),
                          color: Color(0xFF9F140B),
                          child: Text(
                            "Next",
                            style: TextStyle(
                              color: Colors.white,
                              fontSize: 20,
                            ),
                          ),
                        )),
                  ]
              ),
            ),

          ]);
        })
        );
  }
}
