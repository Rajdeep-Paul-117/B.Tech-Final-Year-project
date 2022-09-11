import React from 'react'
import {Dialog,TableContainer,DialogTitle,Table,
  TableHead,TableRow,TableCell,
  Paper,
  TableBody
} from '@mui/material';

function PopUp(props) {
  const {onClose, open,result1,result2 } = props;

  return (
    <Dialog onClose={onClose} open={open}>
      <TableContainer component={Paper}>
      <Table aria-label="customized table">
        <TableHead>
          <TableRow>
            <TableCell style={{backgroundColor:'black', color: 'white',}}>Parameters</TableCell>
            <TableCell style={{backgroundColor:'black', color: 'white',}} align="right">English Language</TableCell>
            <TableCell style={{backgroundColor:'black', color: 'white',}} align="right">Regional Language</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {
          Object.keys(result1).map((key,index) => (
            <TableRow key={index}>
              <TableCell component="th" scope="row">
                {key}
              </TableCell>
              <TableCell align="right">{result1[key]}</TableCell>
              <TableCell align="right">{result2[key]?result2[key]:""}</TableCell>
            </TableRow>
          ))}
            {
          Object.keys(result2).filter((key)=>result1[key]==null).map((key,index) => (
            <TableRow key={index}>
              <TableCell component="th" scope="row">
                {key}
              </TableCell>
              <TableCell align="right">{""}</TableCell>
              <TableCell align="right">{result2[key]}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  </Dialog>
  )
}

export default PopUp