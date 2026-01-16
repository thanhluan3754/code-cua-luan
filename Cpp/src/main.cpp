#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
#define SCREEN_ADDRESS 0x3C

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void printWordSmart(const char* text);
void showLoadingEffect();

struct Word {
  float timestamp;
  const char* text;
  bool newScreen;
};

const Word lyrics[] = {
  {1.09,"Dem",true},{1.73,"mang",false},{2.6,"em",false},{3.07,"ve",false},{3.38,"trong",false},{3.76,"giac",false},{4.19,"mo",false},
  {7.8,"Toi",true},{8.56,"hat",false},{9.47,"len",false},{9.92,"tram",false},{10.22,"loi",false},{10.64,"vu",false},{11.11,"vo",false},
  {14.64,"Van",true},{15.38,"nhung",false},{16.19,"khuon",false},{16.65,"mat",false},{17.05,"cuoi",false},{17.76,"du",false},
  {17.97,"biet",false},{18.43,"se",false},{18.71,"khong",false},{19.15,"he",false},{19.6,"vui",false},
  {21.08,"Du",true},{21.32,"hom",false},{21.58,"nay",false},{21.99,"dau",false},{22.21,"dung",false},{22.59,"sai",false},
  {23.26,"van",false},{23.68,"yeu",false},{23.91,"hon",false},{24.39,"ngay",false},{24.87,"mai",false},
  {27.46,"Xin",true},{27.8,"loi",false},{28.24,"nguoi",false},{28.77,"vi",false},{29.08,"nhung",false},{29.49,"dieu",false},
  {29.9,"chua",false},{30.37,"noi",false},{30.73,"ra",false},{31.17,"thanh",false},{31.65,"cau",false},
  {34.31,"Xin",true},{34.57,"loi",false},{35.05,"nguoi",false},{35.61,"vi",false},{35.87,"bao",false},{36.29,"ngay",false},
  {36.76,"qua",false},{37.28,"da",false},{37.57,"troi",false},{38.07,"ve",false},{38.54,"dau",false},
  {41.12,"Mat",true},{41.4,"bao",false},{41.91,"lau",false},{42.52,"de",false},{42.77,"ta",false},{43.17,"tam",false},
  {43.63,"quen",false},{44.06,"u",false},{44.5,"sau",false},{45.37,"de",false},{45.57,"tim",false},{45.98,"nay",false},
  {46.24,"voi",false},{46.64,"con",false},{47.1,"dau",false},
  {48.7,"Va",true},{48.98,"nhung",false},{49.38,"ky",false},{49.67,"uc",false},{50.04,"met",false},{50.51,"nhoai",false},
  {51.07,"chot",false},{51.47,"tan",false},{51.91,"vao",false},{52.36,"som",false},{52.82,"mai",false}
};

const int totalWords = sizeof(lyrics) / sizeof(lyrics[0]);
unsigned long startTime = 0;
bool isPlaying = false;

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);

  if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    for(;;);
  }

  display.setTextColor(SSD1306_WHITE);
  showLoadingEffect();

  startTime = millis();
  isPlaying = true;
}

void loop() {
  if (!isPlaying) return;

  unsigned long currentMillis = millis();
  float elapsedSeconds = (currentMillis - startTime) / 1000.0;

  static int currentWordIndex = 0;

  if (currentWordIndex < totalWords) {
    Word w = lyrics[currentWordIndex];
    if (elapsedSeconds >= w.timestamp) {
      if (w.newScreen) {
        display.clearDisplay();
        display.setCursor(0, 0);
      }
      printWordSmart(w.text);
      currentWordIndex++;
    }
  } else {
    delay(3000);
    display.clearDisplay();
    display.setCursor(40, 30);
    display.println(F("THE END"));
    display.display();
    isPlaying = false;
  }
}

void printWordSmart(const char* text) {
  int16_t x1, y1;
  uint16_t w, h;
  display.getTextBounds(text, display.getCursorX(), display.getCursorY(), &x1, &y1, &w, &h);

  if (display.getCursorX() + w > SCREEN_WIDTH) {
    display.println();
  }

  display.print(text);
  display.print(" ");
  display.display();
}

void showLoadingEffect() {
  int barWidth = 100;
  int barHeight = 8;
  int x = (SCREEN_WIDTH - barWidth) / 2;
  int y = 40;

  for (int i = 0; i <= 100; i += 2) {
    display.clearDisplay();
    display.setTextSize(1);
    display.setCursor(35, 20);
    display.print(F("LOADING..."));
    display.setCursor(55, 52);
    display.print(i);
    display.print("%");
    display.drawRect(x, y, barWidth, barHeight, SSD1306_WHITE);

    int fillWidth = map(i, 0, 100, 0, barWidth - 4);
    if (fillWidth > 0) {
      display.fillRect(x + 2, y + 2, fillWidth, barHeight - 4, SSD1306_WHITE);
    }

    display.display();
    delay(30);
  }

  delay(500);
  display.clearDisplay();
  display.display();
}
