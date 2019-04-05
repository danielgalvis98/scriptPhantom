const WIDTH = 1600;
const HEIGHT = 900;


var page = require('webpage').create(),
	system = require('system'),
	address, name;


if (system.args.length !== 3) {
	console.log("Format: screen.js [URL] [NameImage]");
	phantom.exit();
}

address = system.args[1];
name = system.args[2];
page.viewportSize = {
  width: WIDTH,
  height: HEIGHT
};

page.open(address, function(){
    setTimeout(function() {
    	try{
    		page.render(name+'.png');
    	}catch (error){
    		console.log("ERROR CONTROLADO BITCH");
    	}
        
        phantom.exit();
    }, 30000);
});

