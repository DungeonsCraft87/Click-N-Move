// Auto-generated code. Do not edit.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);

    helpers._registerFactory("tilemap", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "level":
            case "level1":return tiles.createTilemap(hex`100010000c0c0c0d0c0c0c0708030c0d0c0c0c0c0c010c0b0c010c060a090b010c0d010c0c0c0b010c0d0c060a090c0c0b0c0b0c0b0d0b0c010b0c060a090c0d010c0d0c0c010c0c0d0c0c060a090c0c010c010c0c0c0c0c0c0c0c060a09010b0c0d0c0c070808080808080a0a0a080808080803060a0a0a0a0a0a0a0a0a0a0a0a0a0a09050404040404040a0a0a0404040404020b0c0b0b0c010b060a090b0b0b0d0b0b0b010b0d0b0b0b060a090b010c0b010b0d0c0c0b0c0d0b060a090c0b0c0c0c0d0c0b010b010b0c060a090d0c010b0b0b0c0b0d0c0b0b0b060a090b0b0b0c010b0c010b0b0c010b060a090c010b0c0b0b0b0b0c0b0b0b0b0504020b0b0d0b0b0b`, img`
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
`, [myTiles.transparency16,sprites.castle.tileGrass2,sprites.castle.tilePath9,sprites.castle.tilePath3,sprites.castle.tilePath8,sprites.castle.tilePath7,sprites.castle.tilePath4,sprites.castle.tilePath1,sprites.castle.tilePath2,sprites.castle.tilePath6,sprites.castle.tilePath5,sprites.castle.tileGrass3,sprites.castle.tileGrass1,sprites.builtin.forestTiles0], TileScale.Sixteen);
        }
        return null;
    })

    helpers._registerFactory("tile", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "transparency16":return transparency16;
        }
        return null;
    })

}
// Auto-generated code. Do not edit.
