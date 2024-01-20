import pygame, csv, os 

class Tile(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y
    
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class TileMap():
    def __init__(self, filename): 
        self.tile_size = 20
        self.start_x, self.start_y = 0,0
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map
    
    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename) 
        x, y = 0,0
        for row in map: 
            x=0
            for tile in row: 
                if tile == "-1": #Blank
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                elif tile == "0":
                    tiles.append(Tile("Dark Birck1.png", x * self.tile_size, y*self.tile_size))
                
                x+=1

            y+=1
        
        self.map_w, self.map_h = x*self.tile_size, y*self.tile_size
        return tiles
    