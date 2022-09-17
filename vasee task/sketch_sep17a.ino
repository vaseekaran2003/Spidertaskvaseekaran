#ifndef F_CPU
#define F_CPU 16000000UL
#endif
int i = 0;
unsigned int ubrr = 53;
  
unsigned char data[] = "Fire";

#define SCL_CLOCK  100000 
int tempTC74;
int main(){
  DDRB=(1<<5);
  i2c_init;
  inituart();
  
  
  
  while(1){
    uint8_t data = 0;
  
  i2c_start(0x9A);
  i2c_write(0x00);
  i2c_start(0x9B);
 
  data = i2c_read();
  i2c_stop();
  tempTC74 = data;
  if(tempTC74 >=50){
    
    print_();
    PORTB= (1<<5);
    
    
    
    
    }
    else{

      PORTB=0;
      
      
      }


    

    
    
    
    }
  
  
  }
void i2c_init(void)
{
  
  TWSR = 0;                         
  TWBR = ((F_CPU/SCL_CLOCK)-16)/2; }



unsigned char i2c_start(unsigned char address)
{
    uint8_t   twst;

  
  TWCR = (1<<TWINT) | (1<<TWSTA) | (1<<TWEN);

 
  while(!(TWCR & (1<<TWINT)));

 
  

  
  TWDR = address;
  TWCR = (1<<TWINT) | (1<<TWEN);

 
  while(!(TWCR & (1<<TWINT)));

  
  

}
void i2c_stop(void)
{
   
  TWCR = (1<<TWINT) | (1<<TWEN) | (1<<TWSTO);
  
  
  while(TWCR & (1<<TWSTO));

}
unsigned char i2c_write( unsigned char data )
{ 
    uint8_t   twst;
    
  
  TWDR = data;
  TWCR = (1<<TWINT) | (1<<TWEN);

  
  while(!(TWCR & (1<<TWINT)));

  
  
}
unsigned char i2c_read(void)
{
  TWCR = (1<<TWINT) | (1<<TWEN);
  while(!(TWCR & (1<<TWINT)));
  
    return TWDR;
}
void print_(){ 
  i = 0;
    while(data[i] != 0) /* print the String  "Hello from ATmega328p" */
    {
      while (!( UCSR0A & (1<<UDRE0))); /* Wait for empty transmit buffer       */
      
                       /* When UDRE0 = 0,data transmisson ongoing.                         */
                       /* So NOT{[UCSR0A & (1<<UDRE0)] = 0} = 1 ,While(1) loop stays there */
                       
                       /* When UDRE0 = 1,data transmisson completed.                       */
                       /* So NOT{[UCSR0A & (1<<UDRE0)] = 1} = 0 ,While(0) loop fails       */
                       
      UDR0 = data[i];          /* Put data into buffer, sends the data */
      i++;                             /* increment counter                    */
    }
  
  
  
  }
  void inituart(){
   UBRR0H = (ubrr>>8); // Shift the 16bit value ubrr 8 times to the right and transfer the upper 8 bits to UBBR0H register.
  UBRR0L = (ubrr);    // Copy the 16 bit value ubrr to the 8 bit UBBR0L register,Upper 8 bits are truncated while lower 8 bits are copied
  
  

  UCSR0C = 0x06;       /* Set frame format: 8data, 1stop bit  */
  UCSR0B = (1<<TXEN0)|(1<<RXEN0); /* Enable  transmitter */
  
  
  
  
  
  }
