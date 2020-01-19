package com.example.seniorsaver;

import android.Manifest;
import android.content.pm.PackageManager;
import android.location.Location;
import android.os.Bundle;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.view.View;
import android.view.Menu;
import android.view.MenuItem;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import io.radar.sdk.Radar;
import io.radar.sdk.model.RadarEvent;
import io.radar.sdk.model.RadarUser;

public class MainActivity extends AppCompatActivity {
private static final int ACCESS_FINE_LOCATION_CODE = 100;
private static final int ACCESS_BACKGROUND_LOCATION = 101;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        //Initialising RADAR
        String publishableKey = "prj_test_pk_9a3d304c66917becaf457cdf475503827f9ec36c";
        Radar.initialize(publishableKey);
        String userId = "AppTest";
        Radar.setUserId(userId);

        //Requesting Permissions
        checkpermissions(Manifest.permission.ACCESS_FINE_LOCATION,ACCESS_FINE_LOCATION_CODE);
        checkpermissions(Manifest.permission.ACCESS_BACKGROUND_LOCATION,ACCESS_BACKGROUND_LOCATION);




        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
    public void checkpermissions(String permission, int requestCode) {
        if (ContextCompat.checkSelfPermission(MainActivity.this,
                permission)
                == PackageManager.PERMISSION_DENIED) {
            //Permission is not granted
            ActivityCompat.requestPermissions(MainActivity.this, new String[]{permission}, requestCode);

        }
        //ActivityCompat.requestPermissions(MainActivity.this, new String[] { Manifest.permission.ACCESS_FINE_LOCATION }, requestCode);

    }
    public void locate() {
        Radar.trackOnce(new Radar.RadarCallback() {
            @Override
            public void onComplete(@NotNull Radar.RadarStatus radarStatus, @Nullable Location location, @Nullable RadarEvent[] radarEvents, @Nullable RadarUser radarUser) {

            }
        });
    }
}
