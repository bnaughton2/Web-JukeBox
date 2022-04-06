import React, { Component, useState } from "react";
import {TextField, Button, Grid, Typography } from "@material-ui/core";
import { DataGrid } from '@mui/x-data-grid';

export default function RoomList() {
    //var rows = roomButtonPressed();
    const [columns, setColums] = useState([
      { field: 'id', headerName: 'ID', width: 70 },
      { field: 'code', headerName: 'Code', width: 130 },
      { field: 'host', headerName: 'Host', width: 130 },
      { field: 'guestCanPause', headerName: 'CanPause', width: 100 },
      {
        field: 'votesToSkip',
        headerName: 'NumToSkip',
        type: 'number',
        width: 90,
      },
      { field: 'createdAt', headerName: 'CreatedAt', width: 150 },
    ]);

    const [rows, setRows] = useState([]);
    fetch('/api/list-rooms').then((response) => 
    response.json()
    ).then((data) => setRows(data));

   return (
    <div style={{ height: 400, width: 800}}>
    <Grid container spacing={1}>
    <Grid item xs={12} align="center">
    <div style={{ height: 400, width: 800}}>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={10}
        rowsPerPageOptions={[10]}
        checkboxSelection
        />
        </div>
        </Grid>
        </Grid>
    </div>
);

  }


