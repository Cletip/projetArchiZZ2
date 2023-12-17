function checkform()
{
    
	if (!isFinite(document.inscription.Capital.value))
	{
		// something is wrong
		alert('Rentrez une valeur correct s\'il vous plaît.');
		return false;
	}

	return true;
}