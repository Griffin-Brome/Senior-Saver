package com.example.seniorsaver;

import android.content.Context;

import io.radar.sdk.Radar;
import io.radar.sdk.RadarReceiver;
import io.radar.sdk.model.RadarEvent;
import io.radar.sdk.model.RadarUser;

public class myRadarReceiver extends RadarReceiver {

    //Plan is to geofence places such as nursing homes and frequently visited places.
    //upon leaving or entering a fence a notification would be sent through twilio similar to
    //how we did the help button
    @Override
    public void onEventsReceived(Context context, RadarEvent[] events, RadarUser user) {
        for(RadarEvent event : events){
            event.getType();
        }
    }

    public void onError(Context context, Radar.RadarStatus status) {
        // do something with context, status
    }
}