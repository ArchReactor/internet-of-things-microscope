<?php
   define('BASE_DIR', dirname(__FILE__));
   require_once(BASE_DIR.'/config.php');

   if($_GET["cmd"] == "adv 10") {
      system("sudo /home/pi/Bin/motor_control.py left 200 0.01");
   }
   else if($_GET["cmd"] == "ret 10") {
      system("sudo /home/pi/Bin/motor_control.py right 200 0.01");
   }
   else if($_GET["cmd"] == "foc") {
	$absval = abs($_GET['val']) / 10;
	if ($_GET['val'] < 0) {
		system("sudo /home/pi/Bin/motor_control.py left $absval 0.01");
	}
	else {
		system("sudo /home/pi/Bin/motor_control.py right $absval 0.01");
	}
		
   }
   else {
      $pipe = fopen("FIFO","w");
      fwrite($pipe, $_GET["cmd"]);
      fclose($pipe);
   }
?>
