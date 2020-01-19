package com.example.seniorsaver;

import android.content.Context;

import io.radar.sdk.Radar;
import io.radar.sdk.RadarReceiver;
import io.radar.sdk.model.RadarEvent;
import io.radar.sdk.model.RadarUser;

public class myRadarReceiver extends RadarReceiver {

    @Override
    public void onEventsReceived(Context context, RadarEvent[] events, RadarUser user) {

        user.getId();
    }

    public void onError(Context context, Radar.RadarStatus status) {
        // do something with context, status
    }
}