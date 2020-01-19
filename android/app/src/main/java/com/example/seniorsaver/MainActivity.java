package com.example.seniorsaver;

import android.Manifest;
import android.content.Context;
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
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.TextView;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.w3c.dom.Text;

import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;
import java.time.LocalDateTime;

import io.radar.sdk.Radar;
import io.radar.sdk.model.RadarEvent;
import io.radar.sdk.model.RadarUser;

public class MainActivity extends AppCompatActivity {
private static final String userId = "AppTest";
private static final String publishableKey = "prj_test_pk_9a3d304c66917becaf457cdf475503827f9ec36c";

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        setContentView(R.layout.activity_main);

        //Initialise RADAR
        initialise();

        super.onCreate(savedInstanceState);

        Button helpBtn = (Button) findViewById(R.id.gpsBtn);
        helpBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                help();
            }
        });

    }



    //Sets key and userId, checks permissions
    public void initialise(){
        Radar.initialize(publishableKey);
        Radar.setUserId(userId);
        permissions();
        String[] permissions = new String[] {Manifest.permission.ACCESS_FINE_LOCATION,Manifest.permission.ACCESS_BACKGROUND_LOCATION};

        if (!hasPermissions(this, permissions)) {
            ActivityCompat.requestPermissions(this, permissions, 1);
        }

    }

    public void permissions(){
        String[] permissions = new String[] {Manifest.permission.ACCESS_FINE_LOCATION,Manifest.permission.ACCESS_BACKGROUND_LOCATION};

        if (!hasPermissions(this, permissions)) {
            ActivityCompat.requestPermissions(this, permissions, 2);
        }

    }

    //Used to check permissions
    public static boolean hasPermissions(Context context, String... permissions) {
        if (context != null && permissions != null) {
            for (String permission : permissions) {
                if (ActivityCompat.checkSelfPermission(context, permission) != PackageManager.PERMISSION_GRANTED) {
                    return false;
                }
            }
        }
        return true;
    }


    public void locate() {
        Radar.trackOnce(new Radar.RadarCallback() {
            @Override
            public void onComplete(@NotNull Radar.RadarStatus radarStatus, @Nullable Location location, @Nullable RadarEvent[] radarEvents, @Nullable RadarUser radarUser) {
            //RadarEvent event = new RadarEvent();
                TextView view = (TextView) findViewById(R.id.textView3);
                //view.setText("" + location.getLongitude() + " " + location.getLatitude() + " " + userId + " " + LocalDateTime.now());
                String data = "http://10.0.2.2:5000/help?uid=" + userId + "&lon=" + location.getLongitude() +"&lat=" + location.getLatitude();
                view.setText(data);
                /*try{
                    HttpURLConnection urlConnection = null;
                    URL url = new URL("http://10.0.2.2:5000/help/");
                    urlConnection = (HttpURLConnection) url.openConnection();
                    }catch(Exception e){
                }*/

                /*WebView myWebView = (WebView) findViewById(R.id.webView);
                myWebView.getSettings().setJavaScriptEnabled(true);
                myWebView.loadUrl("www.google.ca");*/
                WebView webView = (WebView)findViewById(R.id.webView);

                webView.setWebViewClient(new WebViewClient() {
                    @Override
                    public boolean shouldOverrideUrlLoading(WebView view, String url) {
                        view.loadUrl(url);
                        return false;
                    }
                });

                webView.loadUrl("http://10.0.2.2:5000/help");



            }
        });
    }


    public void help(){
        locate();
    }
}
