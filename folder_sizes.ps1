$folders = Get-ChildItem "./" | ? {$_.PSIsContainer}

foreach ($f in $folders){
	echo $f
	"{0:N2} MB" -f ((Get-ChildItem $f -Recurse | Where-Object { -not $_.PSIsContainer } | Measure-Object -Property Length -Sum -ErrorAction Stop).Sum / 1MB)
	
}