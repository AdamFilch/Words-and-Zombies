import yaml

config_info = { 
		"assets_path": { "images": {"bulletcount": {"black_bullet": "assets/images/ammo/Bullet_black.png" , "blue_bullet": "assets/images/ammo/Bullet_blue.png"}, 
							  "zombie": { "kenny": "assets/images/zombie/kenny.png", "zombie_kenny": "assets/images/zombie/kenny-zombie.png"}}}, 
		"general_settings": {'screen_width': 800, 'screen_height': 600, "screen_title": "Words and Zombies","bc_sprite_scale": 0.5, "starting_bullet_count": 9, "maximum_zombie": 5}, 
		"testing": {"test_1": 100,"test_2": 200}
	}
	
	

with open("config.yaml", 'w') as yamlfile:
    data = yaml.dump(config_info, yamlfile)
    print("Write successful")