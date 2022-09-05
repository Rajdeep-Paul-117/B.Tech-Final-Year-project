import React from 'react'
import { Box,Grid, TextField,Button} from '@mui/material'
import { useState } from 'react'
import axios from 'axios'
import {v4 as uuid} from 'uuid'

function Editor() {
  const [sourceText, setsourceText] = useState("")

  const baseTextHandler=(e)=>{
    console.log(e.target.value)
  }
  const sourceTextHandler=(e)=>{
    setsourceText(e.target.value)
  }
  
  const translateText=(e)=>{
    const constructed_url = 'https://api.cognitive.microsofttranslator.com/translate'
    const params = {
      'api-version': '3.0',
      'to': 'en'
    }
    const headers = {
      'Ocp-Apim-Subscription-Key': "610f3b1042354f3ea5b3a2a0c1ccaba9",
      'Ocp-Apim-Subscription-Region': "centralindia",
      'Content-type': 'application/json',
      'X-ClientTraceId': uuid()
    }
    const body = [{
      'text': sourceText
  }]
    axios.post(constructed_url,body,{headers:headers,params:params})
    .then(res=>{
      setsourceText(res.data[0].translations[0].text)
    })
    .catch(error=>{
      console.log(error)
    })
  }
  
  return (
    <Box >
    <Grid container mt={5}>
      <Grid item xs={5} m="auto" >
        <TextField 
        id="filled-basic" 
        label="Paste English Text" 
        variant="filled" 
        multiline
        minRows={20}
        fullWidth
        onChange={baseTextHandler}
        />
      </Grid>
      <Grid item xs={5} m="auto">
        <TextField 
        id="filled-basic" 
        label="Paste text of any other language" 
        variant="filled" 
        multiline
        minRows={20}
        fullWidth
        value={sourceText}
        onChange={sourceTextHandler}
        />
      </Grid>
    </Grid>
    <Box mt={3} mb={3}>
    <Button variant="contained" onClick={translateText}>Translate</Button>
    </Box>
    </Box>
  )
}

export default Editor