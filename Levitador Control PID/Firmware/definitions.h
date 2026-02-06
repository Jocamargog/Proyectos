
#include <VL53L0X.h>


// definición de los nucleos en el esp32
#define CORE_0 0   // nucleo base usado por algunas tareas procesador
#define CORE_1 1   // nucleo para el usuario, poner aqui las tareas críticas

// Esta es la configuración del PWM
#define  FREQUENCY_PWM     25000 // frecuencia del pwa
#define  RESOLUTION_PWM    11  // bits del pwm
#define  PIN_PWM          2   // pin del pwm 1
 


float  voltsToPwm =   (pow(2, RESOLUTION_PWM) - 1) / 12; 


//sensor laser
//conectar GPIO 22 SCL
//conectar GPIO 21 a SDA
VL53L0X sensor;


bool setupSensor(void){
    // we set the laser sensor
    sensor.setTimeout(100);  
    if(!sensor.init()){
        printf("No se detecto sensor\n");
        return false;
        }
    sensor.startContinuous(); 
    return true;
}

void setupPwm(void){
    ledcAttach(PIN_PWM,  FREQUENCY_PWM , RESOLUTION_PWM);
    // use las siguientes en PLATTFORMIO en vez de la anterior
    //ledcSetup(0,  FREQUENCY_PWM , RESOLUTION_PWM);
    //ledcAttachPin(PWMPIN, 0);
}

void voltsToFan(float volts){
    uint16_t pwm = volts * voltsToPwm;
    ledcWrite(PIN_PWM , pwm); 
}



