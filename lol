import { Project } from "https://unpkg.com/leopard@^1/dist/index.esm.js";

import Stage from "./Stage/Stage.js";
import Duszek1 from "./Duszek1/Duszek1.js";
import Apple from "./Apple/Apple.js";
import Bananas from "./Bananas/Bananas.js";
import Button1 from "./Button1/Button1.js";

const stage = new Stage({ costumeNumber: 1 });

const sprites = {
  Duszek1: new Duszek1({
    x: -110.03942649342761,
    y: -57.37333383217844,
    direction: 89.9999999999995,
    costumeNumber: 1,
    size: 100,
    visible: true,
    layerOrder: 3
  }),
  Apple: new Apple({
    x: 117,
    y: 115,
    direction: 90,
    costumeNumber: 1,
    size: 100,
    visible: true,
    layerOrder: 2
  }),
  Bananas: new Bananas({
    x: 123,
    y: -8,
    direction: 90,
    costumeNumber: 1,
    size: 100,
    visible: true,
    layerOrder: 1
  }),
  Button1: new Button1({
    x: -7,
    y: 139,
    direction: 90,
    costumeNumber: 1,
    size: 100,
    visible: true,
    layerOrder: 4
  })
};

const project = new Project(stage, sprites, {
  frameRate: 30 // Set to 60 to make your project run faster
});
export default project;
