import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:window_size/window_size.dart';
import 'dart:io' show Platform;
import 'custom_date_range_picker.dart';
import 'provider_state.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  if (Platform.isWindows || Platform.isLinux || Platform.isMacOS) {
    setWindowTitle('Flutter Demo');
    setWindowMinSize(const Size(900, 800));
    setWindowMaxSize(Size.infinite);
  }

  runApp(MultiProvider(
      providers: [ChangeNotifierProvider(create: (context) => ChosenDate()), ChangeNotifierProvider(create: (context) => AvailableRoom())],
      child: MyApp()));
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Namer App',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Color.fromARGB(255, 11, 242, 76)),
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  const MyHomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(image: DecorationImage(fit: BoxFit.cover, image: AssetImage('assets/images/gradient-bg.jpg'))),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        body: Row(
          children: [
            Expanded(flex: 7, child: Calendar()),
            Expanded(
                flex: 3,
                child: Container(
                  decoration:
                      BoxDecoration(color: Color.fromARGB(255, 237, 240, 238), borderRadius: BorderRadius.only(bottomLeft: Radius.circular(30))),
                  child: Padding(
                    padding: const EdgeInsets.only(top: 50, left: 40, right: 40),
                    child: FractionallySizedBox(
                      widthFactor: 1,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            "Available",
                          ),
                          Wrap(direction: Axis.horizontal, children: [
                            for (var room in Provider.of<AvailableRoom>(context).availableRoom)
                              Padding(
                                padding: EdgeInsets.only(right: 20, bottom: 20),
                                child: ConstrainedBox(
                                  constraints: BoxConstraints(minWidth: 50, minHeight: 50, maxWidth: 100),
                                  child: Container(
                                    width: MediaQuery.of(context).size.width * 0.5,
                                    height: 200,
                                    color: room == 2 ? Colors.blueGrey : Colors.blue,
                                    child: Text("Hello"),
                                  ),
                                ),
                              ),
                          ])
                        ],
                      ),
                    ),
                  ),
                )),
          ],
        ),
      ),
    );
  }
}

class Calendar extends StatefulWidget {
  const Calendar({super.key});

  @override
  State<Calendar> createState() => _CalendarState();
}

class _CalendarState extends State<Calendar> {
  DateTime? checkInDate;
  DateTime? checkOutDate;

  @override
  Widget build(BuildContext context) {
    return CustomDateRangePicker(
      primaryColor: Colors.lightBlue,
      backgroundColor: Colors.transparent,
      minimumDate: null,
      maximumDate: null,
    );
  }
}



// OLD DESIGN
// class MyHomePage extends StatelessWidget {
//   const MyHomePage({super.key});

//   @override
//   Widget build(BuildContext context) {
//     return Container(
//       decoration: BoxDecoration(
//           image: DecorationImage(
//               fit: BoxFit.cover,
//               image: AssetImage('assets/images/gradient-bg.jpg'))),
//       child: Scaffold(
//         backgroundColor: Colors.transparent,
//         body: Row(
//           children: [
//             Expanded(
//                 flex: 5,
//                 child: FractionallySizedBox(
//                   widthFactor: 0.85,
//                   heightFactor: 0.5,
//                   child: Column(
//                     children: [
//                       Container(
//                         color: Colors.red,
//                         height: 80,
//                         width: double.infinity,
//                       ),
//                       Expanded(
//                         child: Container(
//                           color: Colors.white,
//                           child: const CheckAvailableForm(),
//                         ),
//                       )
//                     ],
//                   ),
//                 )),
//             Expanded(
//                 flex: 5,
//                 child: Container(
//                   decoration: BoxDecoration(
//                       color: Color.fromARGB(255, 237, 240, 238),
//                       borderRadius:
//                           BorderRadius.only(bottomLeft: Radius.circular(30))),
//                 )),
//           ],
//         ),
//       ),
//     );
//   }
// }

// class CheckAvailableForm extends StatefulWidget {
//   const CheckAvailableForm({super.key});

//   @override
//   State<CheckAvailableForm> createState() => _CheckAvailableFormState();
// }

// class _CheckAvailableFormState extends State<CheckAvailableForm> {
//   DateTime? endDate;
//   DateTime? startDate;

//   @override
//   Widget build(BuildContext context) {
//     return Container(
//       height: 100,
//       child: Column(
//         children: [
//           Container(
//             padding: EdgeInsets.all(16),
//             child: Row(
//               children: [
//                 Expanded(
//                     flex: 5,
//                     child: Padding(
//                       padding: const EdgeInsets.only(right: 8, left: 8),
//                       child: Column(
//                         crossAxisAlignment: CrossAxisAlignment.start,
//                         children: [
//                           Row(
//                             children: [
//                               Icon(Icons.calendar_month),
//                               Padding(
//                                 padding: EdgeInsets.only(left: 10),
//                                 child: Text("Check-In"),
//                               )
//                             ],
//                           ),
//                           TextField(
//                             decoration: InputDecoration(
//                               border: OutlineInputBorder(),
//                               hintText: 'Enter a search term',
//                             ),
//                           ),
//                         ],
//                       ),
//                     )),
//                 Expanded(
//                     flex: 5,
//                     child: Padding(
//                       padding: const EdgeInsets.only(right: 8, left: 8),
//                       child: Column(
//                         crossAxisAlignment: CrossAxisAlignment.start,
//                         children: [
//                           Row(
//                             children: [
//                               Icon(Icons.calendar_month),
//                               Padding(
//                                 padding: EdgeInsets.only(left: 10),
//                                 child: Text("Check-Out"),
//                               )
//                             ],
//                           ),
//                           TextField(
//                             decoration: InputDecoration(
//                               border: OutlineInputBorder(),
//                               hintText: 'Enter a search term',
//                             ),
//                           ),
//                         ],
//                       ),
//                     ))
//               ],
//             ),
//           ),
//           Container(
//             padding: EdgeInsets.all(16),
//             child: Row(
//               children: [
//                 Expanded(
//                     flex: 5,
//                     child: Padding(
//                       padding: const EdgeInsets.only(right: 8, left: 8),
//                       child: Column(
//                         crossAxisAlignment: CrossAxisAlignment.start,
//                         children: [
//                           Row(
//                             children: [
//                               Icon(Icons.man),
//                               Padding(
//                                 padding: EdgeInsets.only(left: 10),
//                                 child: Text("Adults"),
//                               )
//                             ],
//                           ),
//                           TextField(
//                             decoration: InputDecoration(
//                               border: OutlineInputBorder(),
//                               hintText: 'Enter a search term',
//                             ),
//                           ),
//                         ],
//                       ),
//                     )),
//                 Expanded(
//                     flex: 5,
//                     child: Padding(
//                       padding: const EdgeInsets.only(right: 8, left: 8),
//                       child: Column(
//                         crossAxisAlignment: CrossAxisAlignment.start,
//                         children: [
//                           Row(
//                             children: [
//                               Icon(Icons.child_friendly_rounded),
//                               Padding(
//                                 padding: EdgeInsets.only(left: 10),
//                                 child: Text("Kid"),
//                               )
//                             ],
//                           ),
//                           TextField(
//                             decoration: InputDecoration(
//                               border: OutlineInputBorder(),
//                               hintText: 'Enter a search term',
//                             ),
//                           ),
//                         ],
//                       ),
//                     ))
//               ],
//             ),
//           ),
//           Container(
//             padding: EdgeInsets.all(16),
//             child: Row(
//               children: [
//                 Padding(
//                   padding: const EdgeInsets.only(right: 8, left: 8),
//                   child: FilledButton.icon(
//                     onPressed: () => {print("Helo")},
//                     icon: Icon(Icons.search),
//                     label: Text("Search Availability"),
//                     style: ButtonStyle(
//                         backgroundColor:
//                             MaterialStateProperty.resolveWith((states) {
//                           const Set<MaterialState> interactiveStates = {
//                             MaterialState.pressed,
//                             MaterialState.hovered,
//                             MaterialState.focused,
//                           };
//                           if (states.any(interactiveStates.contains)) {
//                             return Colors.blue;
//                           } else {
//                             return Colors.red;
//                           }
//                         }),
//                         // MaterialStateProperty.all(Color(0xff616161)),
//                         shape:
//                             MaterialStateProperty.all<RoundedRectangleBorder>(
//                                 RoundedRectangleBorder(
//                                     borderRadius: BorderRadius.circular(3)))),
//                   ),
//                 ),
//                 Padding(
//                   padding: const EdgeInsets.only(right: 8, left: 8),
//                   child: FilledButton.icon(
//                     onPressed: () => {
//                       showCustomDateRangePicker(
//                         context,
//                         dismissible: true,
//                         minimumDate:
//                             DateTime.now().subtract(const Duration(days: 30)),
//                         maximumDate:
//                             DateTime.now().add(const Duration(days: 30)),
//                         endDate: endDate,
//                         startDate: startDate,
//                         backgroundColor: Colors.white,
//                         primaryColor: Colors.green,
//                         onApplyClick: (start, end) {
//                           setState(() {
//                             startDate = start;
//                             endDate = end;
//                           });
//                         },
//                         onCancelClick: () {
//                           setState(() {
//                             startDate = null;
//                             endDate = null;
//                           });
//                         },
//                       )
//                     },
//                     icon: Icon(Icons.search),
//                     label: Text("Search Availability"),
//                     style: ButtonStyle(
//                         backgroundColor:
//                             MaterialStateProperty.resolveWith((states) {
//                           const Set<MaterialState> interactiveStates = {
//                             MaterialState.pressed,
//                             MaterialState.hovered,
//                             MaterialState.focused,
//                           };
//                           if (states.any(interactiveStates.contains)) {
//                             return Colors.blue;
//                           } else {
//                             return Colors.red;
//                           }
//                         }),
//                         // MaterialStateProperty.all(Color(0xff616161)),
//                         shape:
//                             MaterialStateProperty.all<RoundedRectangleBorder>(
//                                 RoundedRectangleBorder(
//                                     borderRadius: BorderRadius.circular(3)))),
//                   ),
//                 )
//               ],
//             ),
//           ),
//         ],
//       ),
//     );
//   }
// }
