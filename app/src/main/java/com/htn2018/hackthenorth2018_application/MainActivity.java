package com.htn2018.hackthenorth2018_application;

import android.app.Activity;
import android.content.DialogInterface;

import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.provider.MediaStore;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.util.Log;
import android.view.KeyEvent;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;
import android.view.View.OnClickListener;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {

    Button buttonSend, chooseImg, uploadImg;
    EditText textMessage;
    String reason;
    String sentiment;
    ImageView imgView;
    String image;

    public static final int GET_FROM_GALLERY = 3;
    public final static int PICK_PHOTO_CODE = 1046;
    public final int PICK_IMAGE_REQUEST = 1;

    @Override
    public boolean onKeyUp(int keyCode, KeyEvent event) {
        switch (keyCode) {
            case KeyEvent.KEYCODE_D:
                Log.d("RESPONSE", "KEY PRESSED");
                return true;
            case KeyEvent.KEYCODE_F:
                Log.d("RESPONSE", "KEY PRESSED");
                return true;
            case KeyEvent.KEYCODE_J:
                Log.d("RESPONSE", "KEY PRESSED");
                return true;
            case KeyEvent.KEYCODE_K:
                Log.d("RESPONSE", "KEY PRESSED");
                return true;
            default:
                return super.onKeyUp(keyCode, event);
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        buttonSend = (Button) findViewById(R.id.buttonSend);
        textMessage = (EditText) findViewById(R.id.editTextMessage);
        chooseImg = (Button) findViewById(R.id.chooseImg);
        uploadImg = (Button) findViewById(R.id.uploadImg);

        buttonSend.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                Thread thread = new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            OkHttpClient client = new OkHttpClient();
                            MediaType mediaType = MediaType.parse("application/json");
                            String input = textMessage.getText().toString();
                            RequestBody body = RequestBody.create(mediaType, "{\n\t\"message\": \"" + input + "\",\n\t\"image\": \"none\",\n\t\"video\": \"none\"\n}");
                            Request request = new Request.Builder()
                                    .url("https://2b288091.ngrok.io/api/message\n")
                                    .post(body)
                                    .build();
                            Response response = client.newCall(request).execute();

                            String jsonData = response.body().string();
                            JSONObject jsonObject = new JSONObject(jsonData);
                            Log.d("RESPONSE: ", jsonObject.toString());
                            reason = jsonObject.get("place interest").toString();
                            sentiment = jsonObject.get("sentiment analysis").toString();

                            if (sentiment.equals("yellow")) {
                                runOnUiThread(new Runnable() {
                                    @Override
                                    public void run() {
                                        AlertDialog alertDialog = new AlertDialog.Builder(MainActivity.this).create();
                                        alertDialog.setTitle("Yellow Alert");
                                        alertDialog.setMessage("Your input might be controversial because of the words, " + reason + ".\nAre you sure you want to continue?");
                                        alertDialog.setButton(AlertDialog.BUTTON_POSITIVE, "YES",
                                                new DialogInterface.OnClickListener() {
                                                    public void onClick(DialogInterface dialog, int which) {
                                                        textMessage.getText().clear();
                                                        dialog.dismiss();
                                                    }
                                                });
                                        alertDialog.setButton(AlertDialog.BUTTON_NEGATIVE, "NO",
                                                new DialogInterface.OnClickListener() {
                                                    public void onClick(DialogInterface dialog, int which) {
                                                        dialog.dismiss();
                                                    }
                                                });
                                        alertDialog.show();
                                    }
                                });
                            }
                            if (sentiment.equals("red")) {
                                runOnUiThread(new Runnable() {
                                    @Override
                                    public void run() {
                                        AlertDialog alertDialog = new AlertDialog.Builder(MainActivity.this).create();
                                        alertDialog.setTitle("Red Alert");
                                        alertDialog.setMessage("Your input is very controversial because of the words, " + reason + ".\nAre you sure you want to continue?");
                                        alertDialog.setButton(AlertDialog.BUTTON_POSITIVE, "YES",
                                                new DialogInterface.OnClickListener() {
                                                    public void onClick(DialogInterface dialog, int which) {
                                                        textMessage.getText().clear();
                                                        dialog.dismiss();
                                                    }
                                                });
                                        alertDialog.setButton(AlertDialog.BUTTON_NEGATIVE, "NO",
                                                new DialogInterface.OnClickListener() {
                                                    public void onClick(DialogInterface dialog, int which) {
                                                        dialog.dismiss();
                                                    }
                                                });
                                        alertDialog.show();
                                    }
                                });
                            }
                        } catch (Exception e) {
                            Toast.makeText(getApplicationContext(),
                                    "Request failed",
                                    Toast.LENGTH_LONG).show();
                            e.printStackTrace();
                        }
                    }
                });
                thread.start();
            }
        });

        chooseImg.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                Thread thread = new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            OkHttpClient client = new OkHttpClient();
                            MediaType mediaType = MediaType.parse("application/json");
                            String image = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Football_iu_1996.jpg/1200px-Football_iu_1996.jpg";
                            RequestBody body = RequestBody.create(mediaType, "{\n\t\"message\": \"\",\n\t\"image\": \"" + image + "\",\n\t\"video\": \"none\"\n}");
                            Request request = new Request.Builder()
                                    .url("https://2b288091.ngrok.io/api/message\n")
                                    .post(body)
                                    .build();
                            Response response = client.newCall(request).execute();

                            String jsonData = response.body().string();
                            JSONObject jsonObject = new JSONObject(jsonData);
                            Log.d("RESPONSE: ", jsonObject.toString());
                            reason = jsonObject.get("place interest").toString();
                            sentiment = jsonObject.get("sentiment analysis").toString();

                            if (sentiment.equals("yellow")) {
                                runOnUiThread(new Runnable() {
                                    @Override
                                    public void run() {
                                        AlertDialog alertDialog = new AlertDialog.Builder(MainActivity.this).create();
                                        alertDialog.setTitle("Yellow Alert");
                                        alertDialog.setMessage("Your input might be controversial because of the words, " + reason + ".\nAre you sure you want to continue?");
                                        alertDialog.setButton(AlertDialog.BUTTON_POSITIVE, "YES",
                                                new DialogInterface.OnClickListener() {
                                                    public void onClick(DialogInterface dialog, int which) {
                                                        textMessage.getText().clear();
                                                        dialog.dismiss();
                                                    }
                                                });
                                        alertDialog.setButton(AlertDialog.BUTTON_NEGATIVE, "NO",
                                                new DialogInterface.OnClickListener() {
                                                    public void onClick(DialogInterface dialog, int which) {
                                                        dialog.dismiss();
                                                    }
                                                });
                                        alertDialog.show();
                                    }
                                });
                            }
                            if (sentiment.equals("red")) {
                                runOnUiThread(new Runnable() {
                                    @Override
                                    public void run() {
                                        AlertDialog alertDialog = new AlertDialog.Builder(MainActivity.this).create();
                                        alertDialog.setTitle("Red Alert");
                                        alertDialog.setMessage("Your input is very controversial because of the words, " + reason + ".\nAre you sure you want to continue?");
                                        alertDialog.setButton(AlertDialog.BUTTON_POSITIVE, "YES",
                                                new DialogInterface.OnClickListener() {
                                                    public void onClick(DialogInterface dialog, int which) {
                                                        textMessage.getText().clear();
                                                        dialog.dismiss();
                                                    }
                                                });
                                        alertDialog.setButton(AlertDialog.BUTTON_NEGATIVE, "NO",
                                                new DialogInterface.OnClickListener() {
                                                    public void onClick(DialogInterface dialog, int which) {
                                                        dialog.dismiss();
                                                    }
                                                });
                                        alertDialog.show();
                                    }
                                });
                            }
                        } catch (Exception e) {
                            Toast.makeText(getApplicationContext(),
                                    "Request failed",
                                    Toast.LENGTH_LONG).show();
                            e.printStackTrace();
                        }
                    }
                });
                thread.start();
            }
        });

        uploadImg.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                Thread thread = new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            OkHttpClient client = new OkHttpClient();
                            MediaType mediaType = MediaType.parse("application/json");
                            String image = "http://www.simcoemuskokahealth.org/images/default-source/homeslider/istock-174825736-webbanner.jpg?sfvrsn=2";
                            RequestBody body = RequestBody.create(mediaType, "{\n\t\"message\": \"\",\n\t\"image\": \"" + image + "\",\n\t\"video\": \"none\"\n}");
                            Request request = new Request.Builder()
                                    .url("https://2b288091.ngrok.io/api/message\n")
                                    .post(body)
                                    .build();
                            Response response = client.newCall(request).execute();

                            String jsonData = response.body().string();
                            JSONObject jsonObject = new JSONObject(jsonData);
                            Log.d("RESPONSE: ", jsonObject.toString());
                            reason = jsonObject.get("place interest").toString();
                            sentiment = jsonObject.get("sentiment analysis").toString();

                            if (sentiment.equals("yellow")) {
                                runOnUiThread(new Runnable() {
                                    @Override
                                    public void run() {
                                        AlertDialog alertDialog = new AlertDialog.Builder(MainActivity.this).create();
                                        alertDialog.setTitle("Yellow Alert");
                                        alertDialog.setMessage("Your input might be controversial because of the words, " + reason + ".\nAre you sure you want to continue?");
                                        alertDialog.setButton(AlertDialog.BUTTON_POSITIVE, "YES",
                                                new DialogInterface.OnClickListener() {
                                                    public void onClick(DialogInterface dialog, int which) {
                                                        textMessage.getText().clear();
                                                        dialog.dismiss();
                                                    }
                                                });
                                        alertDialog.setButton(AlertDialog.BUTTON_NEGATIVE, "NO",
                                                new DialogInterface.OnClickListener() {
                                                    public void onClick(DialogInterface dialog, int which) {
                                                        dialog.dismiss();
                                                    }
                                                });
                                        alertDialog.show();
                                    }
                                });
                            }
                            if (sentiment.equals("red")) {
                                runOnUiThread(new Runnable() {
                                    @Override
                                    public void run() {
                                        AlertDialog alertDialog = new AlertDialog.Builder(MainActivity.this).create();
                                        alertDialog.setTitle("Red Alert");
                                        alertDialog.setMessage("Your input is very controversial because of the words, " + reason + ".\nAre you sure you want to continue?");
                                        alertDialog.setButton(AlertDialog.BUTTON_POSITIVE, "YES",
                                                new DialogInterface.OnClickListener() {
                                                    public void onClick(DialogInterface dialog, int which) {
                                                        textMessage.getText().clear();
                                                        dialog.dismiss();
                                                    }
                                                });
                                        alertDialog.setButton(AlertDialog.BUTTON_NEGATIVE, "NO",
                                                new DialogInterface.OnClickListener() {
                                                    public void onClick(DialogInterface dialog, int which) {
                                                        dialog.dismiss();
                                                    }
                                                });
                                        alertDialog.show();
                                    }
                                });
                            }
                        } catch (Exception e) {
                            Toast.makeText(getApplicationContext(),
                                    "Request failed",
                                    Toast.LENGTH_LONG).show();
                            e.printStackTrace();
                        }
                    }
                });
                thread.start();
            }
        });
    }
}
