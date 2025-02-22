// 4.2 inch e-Paper demo to display monochrome image

#include "DEV_Config.h"
#include "EPD.h"
#include "GUI_Paint.h"
#include "imagedata.h"
#include <stdlib.h>

UBYTE *Image;
UWORD Imagesize;

void setup()
{
    printf("EPD_4IN2_V2 Demo\r\n");
    DEV_Module_Init();
#if 0
    printf("Init start\r\n");
    EPD_4IN2_V2_Init();
    printf("Init end\r\n");

    printf("Clear start\r\n");
    EPD_4IN2_V2_Clear();
    printf("Clear end\r\n");
#endif

    // Create image cache and fill it with white
    Imagesize = ((EPD_4IN2_V2_WIDTH % 8 == 0)? (EPD_4IN2_V2_WIDTH / 8 ): (EPD_4IN2_V2_WIDTH / 8 + 1)) * EPD_4IN2_V2_HEIGHT;
    printf("Init image start\r\n");
    if ((Image = (UBYTE *)malloc(Imagesize)) == NULL)
    {
        printf("Image memory malloc failed...\r\n");
        while(1);
    }
    Paint_NewImage(Image, EPD_4IN2_V2_WIDTH, EPD_4IN2_V2_HEIGHT, 0, WHITE);
    printf("Init image end\r\n");

    printf("Show monochrome BMP start\r\n");
    // Use fast mode
    EPD_4IN2_V2_Init_Fast(Seconds_1_5S);
    //EPD_4IN2_V2_Init_Fast(Seconds_1S);
    Paint_SelectImage(Image);
    Paint_Clear(WHITE);
    Paint_DrawBitMap(gImage_4in2_mono);
    EPD_4IN2_V2_Display_Fast(Image);
    free(Image);
    Image = NULL;
    printf("Show monochrome BMP end\r\n");

}

void loop()
{
  //
}
