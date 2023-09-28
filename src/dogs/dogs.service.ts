import { Injectable } from '@nestjs/common';
import { CreateDogDto } from './dto/create-dog.dto';
import { UpdateDogDto } from './dto/update-dog.dto';
import { InjectRepository } from '@nestjs/typeorm';
import { Dog } from './entities/dog.entity';
import { Repository } from 'typeorm';

@Injectable()
export class DogsService {
  constructor(
    @InjectRepository(Dog)
    private dogsRepository: Repository<Dog>,
  ) {}

  async create(createDogDto: CreateDogDto) {
    const newDog = this.dogsRepository.create(createDogDto);
    return await this.dogsRepository.save(newDog);
  }

  async findAll() {
    return await this.dogsRepository.find();
  }

  async findOne(id: number) {
    return await this.dogsRepository.findOneBy({ id });
  }

  async update(id: number, updateDogDto: UpdateDogDto) {
    return await this.dogsRepository.update(id, updateDogDto);
  }

  async upsert(updateDogDto: UpdateDogDto) {
    return await this.dogsRepository.upsert([updateDogDto], {
      conflictPaths: ['id'],
      skipUpdateIfNoValuesChanged: true,
    });
  }

  remove(id: number) {
    return this.dogsRepository.delete(id);
  }
}
