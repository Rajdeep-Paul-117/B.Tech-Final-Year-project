import React from 'react'
import { Box,Grid, TextField,Button} from '@mui/material'
import { useState } from 'react'
import axios from 'axios'
import {v4 as uuid} from 'uuid'
import PopUp from './PopUp'
import Result from './Result'

function Editor() {
  const [sourceText, setsourceText] = useState("")
  const [baseText, setbaseText] = useState("")
  const [disable, setDisable] = React.useState(false);
  const [baseArticleResult, setbaseArticleResult] = useState({})
  const [calculation, setcalculation] = useState({})
  const [regionalArticleResult, setregionalArticleResult] = useState({})
  const [showResult, setshowResult] = useState(false) 
  const [showSimilarity, setshowSimilarity] = useState(false)

  const baseTextHandler=(e)=>{
    setbaseText(e.target.value)
  }
  const sourceTextHandler=(e)=>{
    setsourceText(e.target.value)
  }
  const resultClose=(e)=>{
    setshowResult(false)
  }

  const similarityClose=(e)=>{
    setshowSimilarity(false)
  }

  const translateText=(e)=>{
    setDisable(true);
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
  const compareText=(e)=>{
    const url='https://5000-rajdeeppaul-btechfinaly-a9zgjyikrbd.ws-us70.gitpod.io/comp-corenlp'
    //const url='http://localhost:5000/comp-corenlp'
    const body = [{
      'text': baseText
    },
    {
      'text': sourceText
    }
  ]
    axios.post(url,body).then(res=>{
      console.log(res)
      setbaseArticleResult(res.data[0])
      setregionalArticleResult(res.data[1])  
      setshowResult(true)
    }).catch(err=>console.log(err))
    
  }

  const similarity=(e)=>{
    const url='https://5000-rajdeeppaul-btechfinaly-a9zgjyikrbd.ws-us70.gitpod.io/similarity'
    const body = [{
      'text': baseText
    },
    {
      'text': sourceText
    }
  ]
    axios.post(url,body).then(res=>{
      console.log(res) 
      setcalculation(res.data)
      setshowSimilarity(true)
    }).catch(err=>console.log(err))
    
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
    <Button disabled={disable} variant="contained" onClick={translateText}>Translate</Button>
    </Box>
    <Box mt={3} mb={3}>
    <Button  variant="contained" onClick={compareText}>Compare</Button>
    </Box>
    {showResult? <PopUp 
    open={showResult} 
    onClose={resultClose}
    result1={baseArticleResult}
    result2={regionalArticleResult} 
    />:null}

    <Box mt={3} mb={3}>
    <Button  variant="contained" onClick={similarity}>Calculate similarity</Button>
    </Box>
    {showSimilarity? <Result 
    open={showSimilarity} 
    onClose={similarityClose}
    result={calculation}
    />:null}
    </Box>
  )
}

export default Editor