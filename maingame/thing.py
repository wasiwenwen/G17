def make_things(planet_height, PlanetRange):
	#設定第一個障礙物
	thing_startx = random.choice(runway) #X座標從跑道中任選一條
	thing_starty = 0 - planet_height - PlanetRange #因為如果從零開始的話，0會出現在畫面上
	word = random.choice(Picture)
	
	return thing_startx, thing_starty, word
	
thing_startx, thing_starty, word = make_thing(planet_height, PlanetRange * 0)
thing_A_startx, thing_A_starty, word_A = make_thing(planet_height, PlanetRange * 1)
thing_B_startx, thing_B_starty, word_B = make_thing(planet_height, PlanetRange * 2)
thing_C_startx, thing_C_starty, word_C = make_thing(planet_height, PlanetRange * 3)
thing_D_startx, thing_D_starty, word_D = make_thing(planet_height, PlanetRange * 4)

