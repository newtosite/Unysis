#include<ESP8266WiFi.h>
 
const char* ssid = "AndroidAP";
const char* password = "ijwy6841";

uint8_t Pwm1 = 4; //Nodemcu PWM pin 
uint8_t Pwm2 = 5; //Nodemcu PWM pin
 
int a0 = 15;  //Gpio-15 of nodemcu esp8266  
int a1 = 13;  //Gpio-13 of nodemcu esp8266    

WiFiServer server(80);
 
void setup() {
  Serial.begin(9600);
  delay(10);
  pinMode(a0, OUTPUT);      
  pinMode(a1, OUTPUT);     
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
 
  server.begin();
  Serial.println("Server started");
  
  Serial.print("Use this URL to connect: ");
  Serial.print("http://");    //URL IP to be typed in mobile/desktop browser
  Serial.print(WiFi.localIP());
  Serial.println("/"); 
}
void loop() {
  WiFiClient client = server.available();
  if (!client) {
  return;
  }
 
  Serial.println("new client");
  while(!client.available()){
  delay(1);
  }
 
  String request = client.readStringUntil('\r');
  Serial.println(request);
  client.flush();
  
 int Ms=0,dir=0,Pw=0;
   
 digitalWrite(a0, HIGH); 
 digitalWrite(a1, HIGH);

  Ms=1;
  dir=1;
  
  digitalWrite(a0, LOW); 
  digitalWrite(a1, LOW);

 Ms=0;

if (request.indexOf("/Req=2") != -1)  {  
analogWrite(Pwm1, 767);  
analogWrite(Pwm2, 767);  
Pw=1;
}
if (request.indexOf("/Req=3") != -1)  { 
analogWrite(Pwm1, 512);  
analogWrite(Pwm2, 512);  
Pw=2;
}
if (request.indexOf("/Req=4") != -1)  {  
analogWrite(Pwm1, 255);  
analogWrite(Pwm2, 255);  
Pw=3;
}

  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println(""); //  do not forget this one
  client.println("<!DOCTYPE HTML>");
  client.println("<html>");
  client.println("<h1 align=center>SMART TELEMATIC SYSTEM</h1><br><br>");
  client.println("<br><br>");
  client.println("<a href=\"/start=1\"\"><button>Start Motor </button></a><br/>");
  client.println("<a href=\"/stop=1\"\"><button>Stop Motor </button></a><br/>");
  //client.println("<a href=\"/tog=1\"\"><button>Toggle Direction</button></a><br/>");
  client.println("<a href=\"/Req=2\"\"><button> The speed set 80kmph </button></a><br/>");
  client.println("<a href=\"/Req=3\"\"><button>The speed set to 60kmph </button></a><br/>");
  client.println("<a href=\"/Req=4\"\"><button>The speed set to 40kmph</button></a><br/>");
  
  if(Ms==1){
    client.println("Motor Powered Working<br/>" );
    }
    else
    client.println("Motor at Halt<br/>" );
    
  if(dir==1){
    client.println("Motor rotating in forward direction<br/>" );
    }
    else
    client.println("Motor rotating in backward direction<br/>" );

switch(Pw){
      case 1:
        client.println("The speed is 60kmph<br/>" );
        break;
      case 2:
        client.println("The speed is 40kmph<br/>" );
        break;  
      case 3:
        client.println("The speed is 20kmph<br/>" );
        break; 
         
      default:
        client.println("No restrictions<br/>" );
  }
  
  client.println("</html>");
  delay(1);
  Serial.println("Client disonnected");
  Serial.println("");
}
