var btnStart = document.getElementById( "btn-start" );
var btnStop = document.getElementById( "btn-stop" );
var btnCapture = document.getElementById( "btn-capture" );

// The stream & capture
var stream = document.getElementById( "stream" );
var capture = document.getElementById( "capture" );
var snapshot = document.getElementById( "snapshot" );
let model;
// declare a canvas variable and get its context
let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");
var cameraStream = null;

//var error
var error = document.getElementById("error");

// Attach listeners
            btnStart.addEventListener( "click", startStreaming );
            btnStop.addEventListener( "click", stopStreaming );


            // Start Streaming
            function startStreaming() {

                var mediaSupport = 'mediaDevices' in navigator;

                if( mediaSupport && null == cameraStream ) {

                    navigator.mediaDevices.getUserMedia( { video: true } )
                    .then( function( mediaStream ) {

                        cameraStream = mediaStream;

                        stream.srcObject = mediaStream;

                        stream.play();
                    })
                    .catch( function( err ) {

                        console.log( "Unable to access camera: " + err );
                    });
                }
                else {

                    alert( 'Your browser does not support media devices.' );

                    return;
                }
            }

            const detectFaces = async () => {
                const prediction = await model.estimateFaces(stream, false);
                console.log(prediction);
                console.log(prediction.length);
                //console.log(prediction[0].probability[0]);
                
                // draw the video first
                ctx.drawImage(stream, 0, 0, 650, 500);
                // if(prediction.length === 0 )
                // {
                //     var error = document.getElementById("error");
                //     error.innerHTML="No Face Detected!";
                //     console.log(error);
                // }
                if(prediction.length == 0)
                {
                    
                    error.innerHTML="No Face Detected!";
                    console.log(error);
                    setTimeout(timeout, 1000);
                }

                else if(prediction.length > 1 )
                {
                    error.innerHTML="Multiple Faces Detected!";
                    console.log(error);
                    setTimeout(timeout, 1000);
                }
                else if(prediction[0].probability[0] < 0.95)
                {
                   
                    error.innerHTML="Face Not Clear!";
                    console.log(error);
                    setTimeout(timeout, 1000);
                }
                // else if(prediction[0].probability[0] > 0.95 && prediction.length == 1)
                // {
                    
                //     error.innerHTML="Good Angle!";
                //     console.log(error);
                //     setTimeout(timeout, 1000);
                // }
                
                

                prediction.forEach((pred) => {
                  
                  // draw the rectangle enclosing the face
                  ctx.beginPath();
                  ctx.lineWidth = "3";
                  ctx.strokeStyle = "green";
                  // the last two arguments are width and height
                  // since blazeface returned only the coordinates, 
                  // we can find the width and height by subtracting them.
                  ctx.rect(
                    pred.topLeft[0],
                    pred.topLeft[1],
                    pred.bottomRight[0] - pred.topLeft[0],
                    pred.bottomRight[1] - pred.topLeft[1]
                  );
                  ctx.stroke();
                  
                  // drawing small rectangles for the face landmarks
                  // ctx.fillStyle = "red";
                  // pred.landmarks.forEach((landmark) => {
                  //   ctx.fillRect(landmark[0], landmark[1], 5, 5);
                  // });

                  
                });
              };

            function timeout()
            {
                error.innerHTML=" ";
            }


            stream.addEventListener("loadeddata", async () => {
                console.log("Up");
                model = await blazeface.load();
                console.log("Down");
                // call detect faces every 100 milliseconds or 10 times every second
                setInterval(detectFaces, 100);
              });
            // Stop Streaming
            function stopStreaming() {

                if( null != cameraStream ) {

                    var track = cameraStream.getTracks()[ 0 ];

                    track.stop();
                    stream.load();

                    cameraStream = null;
                }
            }

            btnCapture.addEventListener( "click", captureSnapshot );

            function captureSnapshot() 
            {
                if( null != cameraStream ) {

                    var ctx = capture.getContext( '2d' );
                    var img = new Image();

                    ctx.drawImage( stream, 0, 0, capture.width, capture.height );

                    img.src		= capture.toDataURL( "image/png" );
                    img.width	= 240;

                    snapshot.innerHTML = '';

                    snapshot.appendChild( img );
                }
            }
            

            function dataURItoBlob( dataURI ) {

                var byteString = atob( dataURI.split( ',' )[ 1 ] );
                var mimeString = dataURI.split( ',' )[ 0 ].split( ':' )[ 1 ].split( ';' )[ 0 ];
                
                var buffer	= new ArrayBuffer( byteString.length );
                var data	= new DataView( buffer );
                
                for( var i = 0; i < byteString.length; i++ ) {
                
                    data.setUint8( i, byteString.charCodeAt( i ) );
                }
                
                return new Blob( [ buffer ], { type: mimeString } );
            }

            var submit = document.getElementById("signup");
            btnCapture.addEventListener( "click", ImageBase64 );
            var base64_input=document.getElementById("base64");

            const img_name = Math.random().toString(36).substring(2,20);

            function ImageBase64(){
            // var request = new XMLHttpRequest();
            // var csrf=document.getElementsByName("csrfmiddlewaretoken")[0].value;
            // request.open( "POST", "/cam_test/", true );

            // var data	= new FormData();
            var dataURI	= snapshot.firstChild.getAttribute( "src" );
            base64_input.value=dataURI
            var imageData   = dataURItoBlob( dataURI );

            // data.append( "ajax_image", imageData, img_name );
            // data.append("csrfmiddlewaretoken",csrf)
            // request.send( data );
            }