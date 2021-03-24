<div align="center">
  <h1 ><a href="https://writeon.netlify.app/">🎙 Metafrastis-backend 🎙</a></h1>
  <strong>
    Backend For Metafrastis Web and App
  </strong>
</div>
<h1> Description </h1>

An free api to translate your text into any language you want.
### demo using axios
```
const axios = require('axios')

axios.post('https://metafrastis-backend.herokuapp.com/translate', {
    text:"Good Morning",
    lan:"bn"
  })
  .then(function (response) {
    console.log(response);
  })
  
```

### response demo
```
সুপ্রভাত
```
