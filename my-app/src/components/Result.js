import React from 'react'
import {Dialog,TableContainer,DialogTitle,Table,
  TableHead,TableRow,TableCell,
  Paper,
  TableBody
} from '@mui/material';

function Result(props) {
  const {onClose, open,result } = props;

  return (
    <Dialog onClose={onClose} open={open}>
      <TableContainer component={Paper}>
      <Table aria-label="customized table">
        <TableHead>
          <TableRow>
            <TableCell style={{backgroundColor:'black', color: 'white',}}align="center">Cosine Similarity</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          <TableRow>
              <TableCell align="left">
                {result}
              </TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </TableContainer>
  </Dialog>
  )
}

export default Result