import 'package:flutter/material.dart';

class ChosenDate extends ChangeNotifier {
  DateTime? checkInDate;
  DateTime? checkOutDate;

  void changeChosenDate(DateTime? newCheckInDate, DateTime? newCheckOutDate) {
    checkInDate = newCheckInDate;
    checkOutDate = newCheckOutDate;

    notifyListeners();
  }
}

class AvailableRoom extends ChangeNotifier {
  var availableRoom = [1, 2, 3, 4];

  void addAvailableRoom(int roomId) {
    availableRoom.add(roomId);
  }
}
