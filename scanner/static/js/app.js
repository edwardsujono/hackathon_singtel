/**
 * Created by edwardsujono on 20/1/18.
 */

var key_chossen = null;

var app = new Vue({
  el: '#app',
  data: {
    scanner: null,
    activeCameraId: null,
    cameras: [],
    scans: []
  },
  mounted: function () {
    var self = this;

    self.scanner = new Instascan.Scanner({ video: document.getElementById('preview'), scanPeriod: 1 });

    self.scanner.addListener('scan', function (content, image) {
        $("#confirmation").modal('show');
        if(content === "1"){
           window.key_choosen = "DR2009";
           $("#project_key").html("DR2009");
	}else{
           window.key_choosen = "DR2008";
	   $("#project_key").html("DR2008");
        }

    });
    Instascan.Camera.getCameras().then(function (cameras) {
      self.cameras = cameras;
      if (cameras.length > 0) {
        self.activeCameraId = cameras[0].id;
        self.scanner.start(cameras[0]);
      } else {
        console.error('No cameras found.');
      }
    }).catch(function (e) {
      console.error(e);
    });
  },
  methods: {
    formatName: function (name) {
      return name || '(unknown)';
    },
    selectCamera: function (camera) {
      this.activeCameraId = camera.id;
      this.scanner.start(camera);
    }
  }
});
