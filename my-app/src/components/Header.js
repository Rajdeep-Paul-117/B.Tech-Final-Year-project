import React from 'react'
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';

function Header() {
  return (
    <AppBar position="sticky">
    <Toolbar>
      <IconButton
        size="large"
        edge="start"
        color="inherit"
        aria-label="menu"
        sx={{ mr: 2 }}
      >
       
      </IconButton>
      <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
        Multilingual News Article Similarity
      </Typography>
      <Button color="inherit">Login</Button>
    </Toolbar>
  </AppBar>
  )
}

export default Header