/*
 * sensortest.c
 *
 *  Created on: Jan 3, 2024
 *      Author: emre arat
 */

#ifndef SRC_SENSORTEST_C_
#define SRC_SENSORTEST_C_

#include "mpu6050.h"
#include "usbd_cdc_if.h"


static SensorData_t sensorData;



void sensorTest_init(void)
{
    MPU6050_initialize(&sensorData, FS_1000, AFS_4G);
}

void sensorTest_print_acc_values(void)
{
    char buffer[100];
    int32_t len;

    MPU6050_read_data(&sensorData);

    len = sprintf(buffer,"Acc: X:%f Y:%f Z:%f\n",sensorData.acc.X, sensorData.acc.Y, sensorData.acc.Z );
    CDC_Transmit_FS((uint8_t *)buffer, len);
}

void sensorTest_print_gyro_values(void)
{
    char buffer[100];
    int32_t len;

    MPU6050_read_data(&sensorData);

    len = sprintf(buffer,"Gyro: X:%f Y:%f Z:%f\n",sensorData.gyro.X, sensorData.gyro.Y, sensorData.gyro.Z );
    CDC_Transmit_FS((uint8_t *)buffer, len);
}


#endif /* SRC_SENSORTEST_C_ */
