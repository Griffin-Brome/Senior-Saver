package com.example.seniorsaver;

import java.time.LocalDateTime;

public class myEvent {
    double lon, lat;
    String userId;
    LocalDateTime datetime;

    public myEvent(double lon, double lat){
        this.lon = lon;
        this.lat = lat;
        this.datetime = LocalDateTime.now();

    }

}
/*
Might not need to do this, I cant remember how to do this stuff lol
 */