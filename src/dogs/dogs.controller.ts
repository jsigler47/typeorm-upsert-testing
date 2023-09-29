import { Controller, Get, Post, Body, Param, Delete } from '@nestjs/common';
import { DogsService } from './dogs.service';
import { CreateDogDto } from './dto/create-dog.dto';

@Controller('dogs')
export class DogsController {
  constructor(private readonly dogsService: DogsService) {}

  @Post()
  create(@Body() createDogDto: CreateDogDto) {
    return this.dogsService.create(createDogDto);
  }

  @Get()
  findAll() {
    return this.dogsService.findAll();
  }

  // @Get(':id')
  // findOne(@Param('id') id: string) {
  //   return this.dogsService.findOne(+id);
  // }

  // @Patch(':id')
  // update(@Param('id') id: string, @Body() updateDogDto: UpdateDogDto) {
  //   return this.dogsService.update(+id, updateDogDto);
  // }

  @Post('upsert')
  upsert(@Body() updateDogDto: CreateDogDto) {
    return this.dogsService.upsert(updateDogDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.dogsService.remove(id);
  }
}
