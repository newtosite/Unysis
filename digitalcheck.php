<?php
$flag1=0;
$flag2=0;
if($fh=fopen("rc_sri.txt",'r'))
{
	while(!feof($fh))
	{
		$line=fgets($fh);
		echo $line;
		
		echo"<br>";
		if($line=='ADDRESS')
		{
			$flag1=1;
		}
		
	}
	if($flag1==1)
	{
		echo 'it is a licence';
	}
	fclose($fh);
}
?>